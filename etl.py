from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.operators.dummy import DummyOperator
from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from airflow.operators.bash import BashOperator
import pandas as pd

journals_output_path = "/home/airflow/gcs/data/Journals.csv"
final_output_path = "/home/airflow/gcs/data/output.csv"

def remove_first_column():
    df = pd.read_csv(journals_output_path)
   
    # Remove the unnamed column
    df = df.drop(columns=df.columns[df.columns.str.contains('Unnamed')])

    # Save the updated DataFrame back to the CSV file
    df.to_csv(journals_output_path, index=False)

def new_column_thb_price():
    df = pd.read_csv(journals_output_path)
    df['priceTHB'] = df['price'] * 33.96

    # Save the updated DataFrame back to the CSV file
    df.to_csv(final_output_path, index=False)

with DAG(
    "etl",
    start_date=days_ago(1),
    schedule_interval="@once",
    tags=["workshop"]
) as dag:
    t1 = PythonOperator(
        task_id='remove_first_column',
        python_callable=remove_first_column,
        dag=dag
    )

    t2 = PythonOperator(
        task_id='add_new_column_thb_price',
        python_callable=new_column_thb_price,
        dag=dag
    )

    t3 = BashOperator(
        task_id="load_to_bq",
        bash_command="bq load --source_format=CSV --autodetect etl.journal_data gs://your_bucket//data/output.csv",
        dag=dag
    )


    t1 >> t2 >> t3
