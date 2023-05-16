# ETL with GCP

## Dataset: Economics Journal Subscription Data
Dataset Link: [Economics Journal Subscription Data](https://www.kaggle.com/datasets/utkarshx27/economics-journal-subscription-data)

## Overview
This project demonstrates an ETL (Extract, Transform, Load) pipeline using Apache Airflow and Google Cloud Platform (GCP). The pipeline processes the Economics Journal Subscription Data from Kaggle and performs various data transformations before loading it into a target destination.

## Prerequisites
- Apache Airflow installed
- Google Cloud Platform (GCP) project and credentials
- Access to Google Cloud Storage (GCS) and BigQuery

## Pipeline Steps
1. Data Extraction: The Economics Journal Subscription Data is extracted from the provided Kaggle dataset.
2. Data Transformation: The extracted data is processed and transformed using Python and pandas. This includes cleaning the data, removing unnecessary columns, and adding new columns.
3. Data Loading: The transformed data is loaded into Google Cloud Storage (GCS) as a CSV file.
4. Load to BigQuery: The CSV file is loaded into BigQuery, where it can be queried and analyzed.

## Getting Started
1. Clone the repository: `git clone https://github.com/username/reponame.git`
2. Set up the GCP project and configure the necessary credentials.
3. Install Apache Airflow and the required dependencies.
4. Configure Airflow to connect to GCP and set up the necessary connections and variables.
5. Place the Economics Journal Subscription Data CSV file in the designated directory.
6. Start the Airflow scheduler and webserver.
7. Trigger the DAG to run and monitor the progress through the Airflow UI.

## DAG Structure
The main DAG file is `etl.py`, which defines the workflow and tasks for the ETL pipeline. The DAG consists of the following tasks:
- Task 1: Data Extraction
- Task 2: Data Transformation
- Task 3: Data Loading to GCS
- Task 4: Load to BigQuery
![image](https://github.com/thanatkat/ETL-Simple/assets/124798930/d4cfdefa-3d17-4e08-b81f-4216aae24292)
