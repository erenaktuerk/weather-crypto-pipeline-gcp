import unittest
from dags.etl_pipeline import fetch_weather_data, fetch_crypto_data

# Test case class for the ETL pipeline
class TestETLPipeline(unittest.TestCase):

    # Test for the weather data extraction function
    def test_fetch_weather_data(self):
        data = fetch_weather_data()
        self.assertIsNotNone(data)  # Ensure data is not None
        self.assertIn('weather', data)  # Ensure 'weather' field is present in the data

    # Test for the cryptocurrency data extraction function
    def test_fetch_crypto_data(self):
        data = fetch_crypto_data()
        self.assertIsNotNone(data)  # Ensure data is not None
        self.assertIn('bitcoin', data)  # Ensure 'bitcoin' field is present in the crypto data

# Run the tests
if __name__ == '__main__':
    unittest.main()