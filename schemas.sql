-- Create main transactions table
DROP TABLE IF EXISTS transactions;

CREATE TABLE transactions (
    transaction_id VARCHAR(50) PRIMARY KEY,
    user_id VARCHAR(50),
    amount NUMERIC(10,2),
    timestamp TIMESTAMP,
    merchant_category VARCHAR(50),
    is_fraud INT
);
