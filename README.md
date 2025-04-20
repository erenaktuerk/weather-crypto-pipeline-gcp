Weather Crypto Pipeline DAG

Project Overview

This project implements an Apache Airflow Directed Acyclic Graph (DAG) that retrieves weather data, analyzes cryptocurrency prices, transforms and loads the data, and models a decision-making pipeline. The DAG is designed to run periodically and enables structured orchestration for near real-time data processing.

The DAG logic is encapsulated in a reusable ETL module (etl_pipeline.py) and instantiated via weather_crypto_pipeline_dag.py.

⸻

Architecture
	•	Airflow: Orchestrates and schedules the ETL pipeline.
	•	ETL Pipeline: Modular Python code for data extraction, transformation, and loading.
	•	Tasks:
	•	start: Dummy start task.
	•	extract_weather_data: Fetches current weather data from an external API.
	•	extract_crypto_data: Retrieves cryptocurrency market prices.
	•	transform_data: Cleans and merges both data sources.
	•	load_data: Saves the final dataset to a target location.
	•	end: Dummy end task.

⸻

Installation

1. Clone the repository

git clone https://github.com/erenaktuerk/weather-crypto-pipeline-gcp.git
cd weather-crypto-pipeline-gcp



⸻

2. Set up the Python development environment (outside WSL)

This environment is used for writing and testing code (e.g., unit tests, scripts):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt



⸻

3. Set up the Airflow environment inside WSL

Airflow does not run natively on Windows. You must activate this environment inside a WSL terminal (e.g., Ubuntu on Windows):

cd /mnt/c/Users/eren_/OneDrive/Desktop/weather-crypto-pipeline-gcp
python -m venv airflow_env
source airflow_env/bin/activate
pip install -r airflow_requirements.txt

airflow_requirements.txt contains only the dependencies needed to run Airflow and DAGs.

⸻

4. Configure Airflow environment variables in WSL

export AIRFLOW_HOME=~/airflow
export AIRFLOW_CORE_SQL_ALCHEMY_CONN=sqlite:///$AIRFLOW_HOME/airflow.db
export AIRFLOW_CORE_EXECUTOR=LocalExecutor



⸻

5. Initialize the Airflow database

airflow db init



⸻

6. Start the Airflow webserver

airflow webserver --port 8793 --host 0.0.0.0 --access-logfile -



⸻

7. Start the Airflow scheduler

airflow scheduler



⸻

Usage
	•	Open the Airflow web interface at: http://127.0.0.1:8793
	•	Locate the DAG: weather_crypto_pipeline_dag
	•	Enable and trigger the DAG manually or wait for the next scheduled run

⸻

Development & Testing

Run unit tests (in the development environment)

python -m unittest discover tests

These tests validate:
	•	DAG loading
	•	Number and names of tasks
	•	Task dependency structure
	•	Manual DAG triggering

⸻

Extending the DAG
	•	Add new steps to etl_pipeline.py
	•	Register them in weather_crypto_pipeline_dag.py
	•	Update the unit tests in tests/test_dags.py to reflect new logic

⸻

License

This project is licensed under the MIT License.