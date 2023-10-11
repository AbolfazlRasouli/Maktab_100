import unittest, datetime
from unittest.mock import patch
from  server import get_city_weather

class TestWeather(unittest.TestCase):
    @patch('requests.get')
    def test_get_city_weather(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "main": {
                "temp": 25,
                "feels_like": 18
            }
        }

        
        temp, feels_like, now = get_city_weather("Tehran")

        self.assertEqual(temp, 25)
        self.assertEqual(feels_like, 18)
        self.assertIsInstance(now, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
