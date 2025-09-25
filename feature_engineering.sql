-- 1. User-level aggregation
CREATE OR REPLACE VIEW user_agg AS
SELECT 
    user_id,
    COUNT(*) AS total_tx,
    SUM(amount) AS total_amount,
    AVG(amount) AS avg_amount
FROM transactions
GROUP BY user_id;

-- 2. Rolling-window features
CREATE OR REPLACE VIEW user_rolling AS
SELECT 
    user_id,
    COUNT(*) FILTER (WHERE timestamp >= NOW() - INTERVAL '1 day') AS tx_24h,
    COUNT(*) FILTER (WHERE timestamp >= NOW() - INTERVAL '7 days') AS tx_7d,
    COUNT(*) FILTER (WHERE timestamp >= NOW() - INTERVAL '30 days') AS tx_30d
FROM transactions
GROUP BY user_id;

-- 3. Transaction velocity per hour
CREATE OR REPLACE VIEW tx_velocity AS
SELECT 
    user_id,
    DATE_TRUNC('hour', timestamp) AS tx_hour,
    COUNT(*) AS tx_count_hour
FROM transactions
GROUP BY user_id, tx_hour;

-- 4. Behavioral sequence
CREATE OR REPLACE VIEW user_merchant_sequence AS
SELECT 
    user_id,
    STRING_AGG(merchant_category, '->' ORDER BY timestamp) AS merchant_sequence
FROM transactions
GROUP BY user_id;
