from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def extract_weather_data():
    # Funktion zum Abrufen von Wetterdaten
    pass

def extract_crypto_data():
    # Funktion zum Abrufen von Kryptowährungsdaten
    pass

def transform_data():
    # Transformation der Daten
    pass

def load_data():
    # Laden der Daten
    pass

with DAG('etl_pipeline', 
         default_args={'owner': 'airflow', 'start_date': datetime(2025, 4, 18)}, 
         schedule_interval='@daily') as dag:

    start = DummyOperator(task_id='start')
    extract_weather = PythonOperator(task_id='extract_weather_data', python_callable=extract_weather_data)
    extract_crypto = PythonOperator(task_id='extract_crypto_data', python_callable=extract_crypto_data)
    transform = PythonOperator(task_id='transform_data', python_callable=transform_data)
    load = PythonOperator(task_id='load_data', python_callable=load_data)
    end = DummyOperator(task_id='end')

    start >> [extract_weather, extract_crypto] >> transform >> load >> end