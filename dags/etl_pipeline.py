from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import logging

# Define the extraction functions
def extract_weather_data(**kwargs):
    """Function for retrieving weather data"""
    try:
        # Fetch weather data (Placeholder)
        logging.info("Extracting weather data...")
        # You would implement the actual data fetching logic here
    except Exception as e:
        logging.error(f"Failed to extract weather data: {e}")
        raise

def extract_crypto_data(**kwargs):
    """Function for retrieving crypto currency data"""
    try:
        # Fetch crypto data (Placeholder)
        logging.info("Extracting cryptocurrency data...")
        # You would implement the actual data fetching logic here
    except Exception as e:
        logging.error(f"Failed to extract cryptocurrency data: {e}")
        raise

def transform_data(**kwargs):
    """Transformation of data"""
    try:
        # Perform data transformation (Placeholder)
        logging.info("Transforming data...")
        # Implement your data transformation logic here
    except Exception as e:
        logging.error(f"Data transformation failed: {e}")
        raise

def load_data(**kwargs):
    """Load the data to target"""
    try:
        # Load the data (Placeholder)
        logging.info("Loading data...")
        # You would implement the actual data loading logic here
    except Exception as e:
        logging.error(f"Failed to load data: {e}")
        raise

# Define the DAG structure
with DAG(
    'etl_pipeline', 
    default_args={
        'owner': 'airflow', 
        'start_date': datetime(2025, 4, 18), 
        'retries': 1, 
        'retry_delay': timedelta(minutes=5),
    }, 
    schedule_interval='@daily', 
    catchup=False,  # Ensures that missed runs are not backfilled
    tags=['etl', 'weather', 'crypto']
) as dag:

    # Define tasks
    start = EmptyOperator(task_id='start')

    extract_weather = PythonOperator(
        task_id='extract_weather_data', 
        python_callable=extract_weather_data, 
        provide_context=True
    )

    extract_crypto = PythonOperator(
        task_id='extract_crypto_data', 
        python_callable=extract_crypto_data, 
        provide_context=True
    )

    transform = PythonOperator(
        task_id='transform_data', 
        python_callable=transform_data, 
        provide_context=True
    )

    load = PythonOperator(
        task_id='load_data', 
        python_callable=load_data, 
        provide_context=True
    )

    end = EmptyOperator(task_id='end')

    # Define the task dependencies
    start >> [extract_weather, extract_crypto] >> transform >> load >> end