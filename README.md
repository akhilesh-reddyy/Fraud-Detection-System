# Fraud Detection System using SQL and Machine Learning

## Project Overview

This project builds a fraud detection system leveraging SQL for feature engineering and Python-based ML for prediction. The goal is to detect potentially fraudulent transactions in financial datasets by integrating database-level feature aggregation with advanced ML models.

Recruiters and hiring managers will immediately see that this project demonstrates:

Advanced SQL feature engineering for real-world transactional data.

ML modeling and evaluation for imbalanced classification problems.

Integration of SQL with Python workflows to create a production-ready pipeline.

Explainable AI (XAI) for actionable insights.

## Problem Statement

Financial institutions need robust systems to detect fraudulent transactions to minimize loss and protect users. Traditional rule-based methods often fail to capture complex patterns. This project addresses this by:

Aggregating transaction data using SQL queries.

Engineering features capturing transaction velocity, user behavior, and anomaly patterns.

Applying supervised ML models to predict fraud probability.

Providing interpretable insights using SHAP values.

## Dataset

Source: [Credit Card Fraud Detection Dataset (Kaggle)]()

Description:

transaction_id: Unique identifier

user_id: User identifier

amount: Transaction amount

timestamp: Transaction date/time

merchant_category: Merchant category code

is_fraud: Fraud label (1 = fraud, 0 = legit)

## SQL Feature Engineering

The project demonstrates advanced SQL skills by creating multiple views for feature extraction:

1. User-level aggregation:
   * Total transactions, total and average amounts per user.

3. Rolling-window features:
   * Transactions in last 24 hours, 7 days, 30 days.

   * Rolling average transaction amount over last 5 transactions.

3.Velocity and anomaly features

   * Transactions per hour.

   * Patterns across merchants or multi-account activity.
  
## Machine Learning Pipeline

Models Used: Random Forest (with class balancing for imbalanced data)

Workflow:

Pull feature data from SQL using pandas.read_sql.

Merge and clean feature tables.

Standardize numeric features.

Train/test split (stratified for fraud labels).

Train model, tune hyperparameters.

Evaluate using metrics:

Precision, Recall, F1-score (focus on recall for fraud)

ROC-AUC score

Confusion matrix

SHAP or LIME used to identify which SQL-engineered features contribute most to fraud prediction.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Production-Ready Integration

This project goes beyond a standard ML pipeline by demonstrating:

Automated SQL feature extraction (daily or real-time).

Writing predictions back to SQL tables for operational use.

Triggering alerts for high-risk transactions.

Visualization dashboards for monitoring fraud patterns.
