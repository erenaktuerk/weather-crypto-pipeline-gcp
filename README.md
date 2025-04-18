# Weather Crypto Pipeline DAG

## Project Overview

This project implements an Airflow Directed Acyclic Graph (DAG) that retrieves weather data, analyzes cryptocurrency prices, and provides a decision-making pipeline. The DAG is designed to run periodically to process real-time data and make informed decisions.

## Architecture

- *Airflow*: Orchestrates the execution of the pipeline.
- *Gunicorn*: Acts as the WSGI server for the web interface.
- *DAG*: Defines the steps of the pipeline, including fetching weather data, analyzing cryptocurrency prices, and making decisions.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/weather-crypto-pipeline.git
   cd weather-crypto-pipeline

	2.	Create and activate a virtual Python environment:

python -m venv airflow_env
source airflow_env/bin/activate  # On Windows: airflow_env\Scripts\activate


	3.	Install the required packages:

pip install -r requirements.txt


	4.	Set the environment variables for Airflow:

export AIRFLOW_HOME=~/airflow
export AIRFLOW_CORE_SQL_ALCHEMY_CONN=sqlite:///$AIRFLOW_HOME/airflow.db
export AIRFLOW_CORE_EXECUTOR=LocalExecutor


	5.	Initialize the Airflow database:

airflow db init


	6.	Start the Airflow webserver:

airflow webserver --port 8793 --host 0.0.0.0 --access-logfile -


	7.	Start the Airflow scheduler:

airflow scheduler



Usage
	•	Access the Airflow web interface at http://127.0.0.1:8793.
	•	Check the status of the DAG weather_crypto_pipeline_dag.
	•	Trigger the DAG manually or wait for the next scheduled run.

Development
	•	Ensure all tests pass:

pytest


	•	Add new operators or sensors to extend the pipeline.
	•	Document all changes in the changelog.

License

This project is licensed under the MIT License.

---