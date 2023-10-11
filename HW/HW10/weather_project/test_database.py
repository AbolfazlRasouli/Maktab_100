import unittest
from database import WeatherDatabase


class DataTest(unittest.TestCase):
    def test_connect(self):
        weather_object = WeatherDatabase()
        weather_object.save_request_data('tehran', '1402')
    
        
        


if __name__ == '__main__':
    unittest.main()