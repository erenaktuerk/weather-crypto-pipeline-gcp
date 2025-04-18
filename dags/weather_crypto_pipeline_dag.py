# Import necessary Airflow modules
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

# Function to fetch weather data, executed by PythonOperator
def fetch_weather_data():
    print("Fetching weather data...")

# Function to fetch cryptocurrency data, executed by PythonOperator
def fetch_crypto_data():
    print("Fetching cryptocurrency data...")

# Function to process the fetched data, executed by PythonOperator
def process_data():
    print("Processing data...")

# Function to store the processed results, executed by PythonOperator
def store_results():
    print("Storing results...")

# Define the DAG
dag = DAG(
    'weather_crypto_pipeline_dag',  # Name of the DAG
    description='Pipeline for fetching and processing weather and cryptocurrency data',
    schedule_interval=None,  # No regular schedule, will be triggered manually
    start_date=datetime(2025, 4, 18),  # Start date
    catchup=False,  # Do not perform backfills
)

# Define the tasks
start_task = EmptyOperator(
    task_id='start',  # Task ID
    dag=dag,
)

fetch_weather_task = PythonOperator(
    task_id='fetch_weather_data',  # Task ID
    python_callable=fetch_weather_data,  # Function to be executed
    dag=dag,
)

fetch_crypto_task = PythonOperator(
    task_id='fetch_crypto_data',  # Task ID
    python_callable=fetch_crypto_data,  # Function to be executed
    dag=dag,
)

process_data_task = PythonOperator(
    task_id='process_data',  # Task ID
    python_callable=process_data,  # Function to be executed
    dag=dag,
)

store_results_task = PythonOperator(
    task_id='store_results',  # Task ID
    python_callable=store_results,  # Function to be executed
    dag=dag,
)

# Set the task dependencies
start_task >> [fetch_weather_task, fetch_crypto_task]  # Start task leads to both data fetching tasks
fetch_weather_task >> process_data_task  # Weather data fetch task leads to data processing
fetch_crypto_task >> process_data_task  # Crypto data fetch task leads to data processing
process_data_task >> store_results_task  # Data processing task leads to storing results