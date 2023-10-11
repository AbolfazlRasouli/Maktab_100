import socket
import datetime
import database

clinet_Weather = database.WeatherDatabase()

def start_client(user_input) :
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    HOST = "127.0.0.1"
    PORT = 8500
    client.connect((HOST, PORT))

    client.send(user_input.encode('utf-8'))
    data_client = client.recv(1024).decode('utf-8')
    return data_client


def time_now():
    date_time = datetime.datetime.now()
    format_date = date_time.strftime('%Y-%m-%d %H:%M:%S')
    return format_date

def get_database():
   
    count_request = str(clinet_Weather.get_request_count()).strip("()").replace(",", "")
    count_request_succes = str(clinet_Weather.get_successful_request_count()).strip("()").replace(",", "")
    list_all_response = clinet_Weather.get_all_response()
    
    
    return count_request, count_request_succes, list_all_response





while True:

    user_input = input('Enter the name of the city :')

    if user_input == 'exite':
        break

    result_date = time_now()
    result_request = start_client(user_input)
    clinet_Weather.save_request_data(user_input, result_date)
  

    if result_request == 'city not find':
        print('Invalid city --> Error retrieving weather data: no matching location found.')
        
        
        clinet_Weather.save_response_date("invalid", result_date)
        
    else:
        result_request_tuple = tuple(item for item in result_request.strip("()").split(","))
        city, temperature, feels_link = result_request_tuple
        clinet_Weather.save_response_date(city, result_date, float(temperature), float(feels_link))
        print(f'city: {city}')
        print(f'Temperature: {temperature}')
        print(f'Feels Link: {feels_link}')
        print(f'Last Update: {result_date}')


count_request, count_request_succes, list_response = get_database()
print(f'Request count : {count_request}')
print(f'Successful request count : {count_request_succes}')
print(f'City Request count : {list_response}')



























# date = datetime.datetime.now()
# formatted_date = date.strftime('%Y-%m-%d %H:%M:%S')
# print(type(formatted_date))
# print(formatted_date)

        
    
    
        
