from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from etl_pipeline import (
    extract_weather_data,
    extract_crypto_data,
    transform_data,
    load_data
)

# Default DAG arguments
default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 4, 18),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# DAG definition
with DAG(
    dag_id="weather_crypto_pipeline_dag",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
    tags=["etl", "weather", "crypto"]
) as dag:

    # Dummy task to indicate start of pipeline
    start = EmptyOperator(task_id="start")

    # Extraction tasks
    extract_weather = PythonOperator(
        task_id="extract_weather_data",
        python_callable=extract_weather_data
    )

    extract_crypto = PythonOperator(
        task_id="extract_crypto_data",
        python_callable=extract_crypto_data
    )

    # Transformation task
    transform = PythonOperator(
        task_id="transform_data",
        python_callable=transform_data
    )

    # Load task
    load = PythonOperator(
        task_id="load_data",
        python_callable=load_data
    )

    # Dummy task to indicate end of pipeline
    end = EmptyOperator(task_id="end")

    # Task dependencies
    start >> [extract_weather, extract_crypto] >> transform >> load >> end