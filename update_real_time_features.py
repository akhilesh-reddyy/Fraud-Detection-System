import psycopg2
from apscheduler.schedulers.blocking import BlockingScheduler

def update_real_time_features():
    conn = psycopg2.connect("dbname='fraud_db' user='user' password='pass' host='localhost'")
    cur = conn.cursor()
    # Update rolling features every 5 minutes
    cur.execute("""
        CREATE OR REPLACE VIEW user_last_24h AS
        SELECT 
            user_id,
            COUNT(*) AS tx_count_24h,
            SUM(amount) AS tx_total_24h
        FROM transactions
        WHERE timestamp >= NOW() - INTERVAL '1 day'
        GROUP BY user_id;
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("Updated real-time features")

scheduler = BlockingScheduler()
scheduler.add_job(update_real_time_features, 'interval', minutes=5)
scheduler.start()
