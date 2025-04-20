import unittest
from airflow.models import DagBag

class TestETLPipeline(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Load DAGs from the specified DAG folder and initialize the DagBag.
        """
        cls.dagbag = DagBag(dag_folder='C:\\Users\\eren_\\OneDrive\\Desktop\\weather-crypto-pipeline-gcp\\dags')

        # Raise exception if any DAG import errors exist
        if cls.dagbag.import_errors:
            raise Exception(f"Import errors: {cls.dagbag.import_errors}")

        # Retrieve the DAG by its ID
        cls.dag = cls.dagbag.get_dag('weather_crypto_pipeline_dag')
        if cls.dag is None:
            raise Exception("DAG not found. Check the DAG ID.")

    def test_dag_loaded(self):
        """Ensure the DAG was loaded properly"""
        self.assertIsNotNone(self.dag, "DAG should be loaded")

    def test_task_count(self):
        """Check that the DAG has exactly 6 tasks"""
        self.assertEqual(len(self.dag.tasks), 6, "Expected 6 tasks in the DAG")

    def test_task_names(self):
        """Check that the DAG contains all expected task IDs"""
        expected_tasks = [
            'start',
            'extract_weather_data',
            'extract_crypto_data',
            'transform_data',
            'load_data',
            'end'
        ]
        dag_tasks = [task.task_id for task in self.dag.tasks]
        for task_id in expected_tasks:
            self.assertIn(task_id, dag_tasks, f"Task '{task_id}' is missing from DAG")

    def test_task_dependencies(self):
        """Verify task dependency structure in the DAG"""
        # Define expected task dependencies
        expected_dependencies = {
            'start': ['extract_weather_data', 'extract_crypto_data'],
            'extract_weather_data': ['transform_data'],
            'extract_crypto_data': ['transform_data'],
            'transform_data': ['load_data'],
            'load_data': ['end']
        }

        for upstream, downstream_list in expected_dependencies.items():
            for downstream in downstream_list:
                self.assertIn(
                    downstream,
                    [t.task_id for t in self.dag.get_task(upstream).downstream_list],
                    f"{downstream} should be downstream of {upstream}"
                )

    def test_dag_run(self):
        """Test that the DAG can be triggered manually"""
        try:
            dag_run = self.dag.create_dagrun(
                run_id="test_manual_run",
                execution_date=self.dag.default_args['start_date'],
                state="running",
                conf={},
                external_trigger=False
            )
            self.assertIsNotNone(dag_run)
            self.assertEqual(dag_run.state, "running")
        except Exception as e:
            self.fail(f"Failed to create DAG run: {e}")

if __name__ == '__main__':
    unittest.main()