import pandas as pd
import psycopg2
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib

# Connect to DB
conn = psycopg2.connect("dbname='fraud_db' user='user' password='pass' host='localhost'")

# Pull features
query = """
SELECT t.transaction_id, t.user_id, t.amount, t.is_fraud,
       ua.total_tx, ua.total_amount, ua.avg_amount,
       ur.tx_24h, ur.tx_7d, ur.tx_30d
FROM transactions t
LEFT JOIN user_agg ua ON t.user_id = ua.user_id
LEFT JOIN user_rolling ur ON t.user_id = ur.user_id
"""
df = pd.read_sql(query, conn)
conn.close()

# Preprocess
features = ['amount','total_tx','total_amount','avg_amount','tx_24h','tx_7d','tx_30d']
X = df[features]
y = df['is_fraud']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train model
model = RandomForestClassifier(class_weight='balanced', n_estimators=100, random_state=42)
model.fit(X_scaled, y)

# Save model
joblib.dump(model, 'rf_fraud_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

# Make predictions
df['fraud_prob'] = model.predict_proba(X_scaled)[:,1]

# Optionally write predictions back to DB
conn = psycopg2.connect("dbname='fraud_db' user='user' password='pass' host='localhost'")
cur = conn.cursor()
for idx, row in df.iterrows():
    cur.execute("""
        UPDATE transactions SET fraud_prob = %s WHERE transaction_id = %s
    """, (float(row['fraud_prob']), row['transaction_id']))
conn.commit()
cur.close()
conn.close()
