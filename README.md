# Fraud Detection System using SQL and Machine Learning

## Project Overview

This project builds a fraud detection system by combining SQL-based feature engineering with Python machine learning models. The goal is to identify potentially fraudulent transactions in financial datasets by integrating database-level aggregation with advanced ML techniques.

## Problem Statement

Financial institutions require robust fraud detection systems to minimize losses and protect users. Traditional rule-based methods often fail to detect complex fraud patterns.

This project solves the problem by:

* Aggregating transactional data using SQL queries.

* Engineering features capturing transaction velocity, user behavior, and anomaly patterns.

* Applying supervised ML models to predict fraud probability.

* Providing interpretable insights using SHAP values.
  
## Dataset

Source: [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

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
   * Total and average transaction amounts per user

2. Rolling-window features:
   * Transactions in last 24 hours, 7 days, 30 days.

   * Rolling average transaction amount over last 5 transactions.

3.Velocity and anomaly features

   * Transactions per hour.

   * Patterns across merchants or multi-account activity.

4. Real-Time / Streaming Features
   * Python scheduler updates rolling features in real-time for operational scoring.

5. Behavioral Feature Engineering
   * User transaction sequences: detect unusual order of merchant categories
   * Feature interactions: combine velocity, merchant category, and location for advanced patterns
  
## Machine Learning Pipeline

Models Used: Random Forest (with class balancing for imbalanced data)

Workflow:

1. Pull feature data from SQL using pandas.read_sql

2. Merge and clean feature tables

3. Standardize numeric features

4. Train/test split (stratified by fraud labels)

5. Train model and tune hyperparameters

6. Evaluate using metrics:

   * Precision, Recall, F1-score (focus on Recall for fraud)

   * ROC-AUC score

   * Confusion matrix

7. Apply SHAP or LIME to interpret which SQL-engineered features contribute most to fraud prediction

## Production-Ready Integration

* Automated SQL feature extraction (daily or real-time)

* Writing predictions back to SQL tables for operational use

* Triggering alerts for high-risk transactions

* Visualization dashboards for monitoring fraud patterns
