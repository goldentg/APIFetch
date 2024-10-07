import unittest
from unittest.mock import patch
import API.WeatherAPI as WeatherAPI

class TestWeatherAPI(unittest.TestCase):

    @patch('API.WeatherAPI.requests.get')
    def test_getWeatherByCity(self, mock_get):
        # Mock the API response
        mock_response = {
            "name": "Test City",
            "weather": [{"description": "clear sky"}],
            "main": {
                "temp": 293.15,
                "feels_like": 293.15,
                "pressure": 1013,
                "humidity": 53
            },
            "wind": {"speed": 1.5}
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        # Call the function
        result = WeatherAPI.getWeatherByCity()

        # Check if the result is a dictionary (JSON formatted data)
        self.assertIsInstance(result, dict)
        # Check if the dictionary contains expected keys
        self.assertIn("name", result)
        self.assertIn("weather", result)
        self.assertIn("main", result)
        self.assertIn("wind", result)

    def test_formatWeatherData(self):
        weather_data = {
            "name": "Test City",
            "weather": [{"description": "clear sky"}],
            "main": {
                "temp": 293.15,
                "feels_like": 293.15,
                "pressure": 1013,
                "humidity": 53
            },
            "wind": {"speed": 1.5}
        }

        # Test with metric units
        result_metric = WeatherAPI.formatWeatherData(weather_data, "metric")
        self.assertIn("City: Test City", result_metric)
        self.assertIn("Conditions: clear sky", result_metric)
        self.assertIn("Temperature:", result_metric)
        self.assertIn("Feels Like:", result_metric)
        self.assertIn("Humidity:", result_metric)
        self.assertIn("Wind Speed:", result_metric)
        self.assertIn("Pressure:", result_metric)

        # Test with imperial units
        result_imperial = WeatherAPI.formatWeatherData(weather_data, "imperial")
        self.assertIn("City: Test City", result_imperial)
        self.assertIn("Conditions: clear sky", result_imperial)
        self.assertIn("Temperature:", result_imperial)
        self.assertIn("Feels Like:", result_imperial)
        self.assertIn("Humidity:", result_imperial)
        self.assertIn("Wind Speed:", result_imperial)
        self.assertIn("Pressure:", result_imperial)

if __name__ == '__main__':
    unittest.main()