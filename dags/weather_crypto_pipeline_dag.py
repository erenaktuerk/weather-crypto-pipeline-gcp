from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime
import requests

# Function to fetch weather data from OpenWeather API
def fetch_weather_data():
    # Using a dummy API key for demonstration purposes
    api_key = 'dummy_api_key_1234567890'  # Replace with your real key if needed
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q=London&appid={api_key}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching weather data: {response.status_code}")
        return None

# Function to fetch cryptocurrency data from CoinGecko API
def fetch_crypto_data():
    # CoinGecko API does not require an API key
    api_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching crypto data: {response.status_code}")
        return None

# Function to process the fetched data (placeholder logic)
def process_data():
    print("Processing data...")  # This is where data processing logic would go

# Function to store the processed results (placeholder logic)
def store_results():
    print("Storing results...")  # This is where storing logic would go

# Define the Airflow DAG
dag = DAG(
    'weather_crypto_pipeline_dag',  # DAG name
    description='ETL pipeline for weather and cryptocurrency data',
    schedule_interval=None,  # No automatic schedule, run manually
    start_date=datetime(2025, 4, 18),
    catchup=False,
)

# Define tasks in the DAG
start_task = EmptyOperator(task_id='start', dag=dag)

fetch_weather_task = PythonOperator(
    task_id='fetch_weather_data',
    python_callable=fetch_weather_data,
    dag=dag,
)

fetch_crypto_task = PythonOperator(
    task_id='fetch_crypto_data',
    python_callable=fetch_crypto_data,
    dag=dag,
)

process_data_task = PythonOperator(
    task_id='process_data',
    python_callable=process_data,
    dag=dag,
)

store_results_task = PythonOperator(
    task_id='store_results',
    python_callable=store_results,
    dag=dag,
)

# Define task dependencies
start_task >> [fetch_weather_task, fetch_crypto_task]  # Start triggers both data fetches
fetch_weather_task >> process_data_task  # Weather data flows into processing
fetch_crypto_task >> process_data_task  # Crypto data flows into processing
process_data_task >> store_results_task  # Processed data is stored