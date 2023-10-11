import socket

import requests

import pprint



def get_city_weather(city):
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
        temperature = data["main"]["temp"]
        feels_link = data["main"]["feels_like"]

        
        return city,temperature, feels_link
    else :
        return 'city not find'
    


def start_server():

    server_soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    HOST = "127.0.0.1"
    PORT = 8500
    server_soket.bind((HOST, PORT))
    server_soket.listen(1)

    print('Connected to the server')
    while True :
        connection, address = server_soket.accept()
        data = connection.recv(1024).decode('utf-8')
        result = get_city_weather(data)
        # print(f'{data} : {result}')
        connection.send(str(result).encode('utf-8'))
        connection.close()


start_server()











            

# # london
# input_city = input('Enter name city : ')
# result = get_weather_data(input_city)
# print(result)