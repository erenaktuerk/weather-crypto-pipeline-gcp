import unittest
from dags.etl_pipeline import extract_weather_data, extract_crypto_data

class TestETLPipeline(unittest.TestCase):

    def test_extract_weather_data(self):
        data = extract_weather_data()
        self.assertIsNotNone(data)

    def test_extract_crypto_data(self):
        data = extract_crypto_data()
        self.assertIsNotNone(data)

if __name__ == '__main__':
    unittest.main()