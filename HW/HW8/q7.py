import requests
from bs4 import BeautifulSoup
import pprint


def get_weather_data(city):
    api_key = "c07c243246aca1f8230055d5e4185f8b"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        # pprint.pprint(response.json())
    except KeyError as e:
        print(f"Error {e}")
    except Exception as e:
        print(f"an error occurred: {e}") 
    if response.status_code == 200 :
        data = response.json()
        temperature= data["main"]["temp"]
        
        return f'temperature city {city} : {temperature}'
    else :
        return f'city {city} not find'
            

# london
input_city = input('Enter name city : ')
result = get_weather_data(input_city)
print(result)





