# AWS ETL Pipeline for Daily Bank Transactions

🚀 Welcome to my robust ETL (Extract, Transform, Load) pipeline for processing daily bank transactions using Amazon Web Services (AWS).

## Overview

This project implements a scalable and serverless ETL pipeline for handling daily bank transactions. The entire process is orchestrated using various AWS services to ensure efficiency, reliability, and security.

## Project Breakdown

### 1️⃣ Data Ingestion

- **Source Data:** Daily CSV files are uploaded to an S3 bucket (`s3://your-source-bucket`).

### 2️⃣ Serverless Trigger

- **AWS Lambda Function:** A serverless AWS Lambda function is triggered upon the upload of CSV files. This Lambda function initiates the execution of the AWS Glue job.

### 3️⃣ Data Transformation

- **AWS Glue Job:** The AWS Glue job is responsible for processing the data. It leverages bookmarking for efficient incremental loads, ensuring that only new data is processed.

### 4️⃣ Storage

- **Processed Data:** The transformed data is securely stored in another S3 bucket (`s3://your-destination-bucket`) in the efficient Parquet format.

### 5️⃣ Analysis

- **Athena for Analysis:** AWS Athena is employed for seamless analysis of the transformed data. Users can run SQL queries on the Parquet data stored in the destination S3 bucket.

