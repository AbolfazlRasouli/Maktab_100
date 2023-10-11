import psycopg2
from typing import List, Tuple

class WeatherDatabase :

    def save_request_data(self, city_name: str, request_time: str) :

        try :
            connection = psycopg2.connect(
            host = "localhost",
            database = "ServerApi",
            user = "postgres",
            password = "123456zx" 
            )
            cursoring = connection.cursor()

            pg_insert = """ INSERT INTO public."request"(
            "city_name", "request_time")
            VALUES(%s, %s)"""

            inserted_values = (
                city_name,
                request_time
            )
            
            cursoring.execute(pg_insert, inserted_values)
            connection.commit()
           

        except Exception as e :
            print(e)

        finally:
            if connection :
                cursoring.close()
                connection.close()
                



    def save_response_date(self, city_name, last_update, temp=0, feels_like=0) :

        try :
            connection = psycopg2.connect(
            host = "localhost",
            database = "ServerApi",
            user = "postgres",
            password = "123456zx" 
            )
            cursoring = connection.cursor()

            pg_insert = """ INSERT INTO public."response"(
            "city_name", "temp_response", "feels_like", "last_update")
            VALUES(%s, %s, %s, %s)"""

            inserted_values = (
                city_name,
                temp,
                feels_like,
                last_update
            )
            
            cursoring.execute(pg_insert, inserted_values)
            connection.commit()
            

        except Exception as e :
            print(e)

        finally:
            if connection :
                cursoring.close()
                connection.close()
               



    def get_request_count(self):
        try :
            connection = psycopg2.connect(
            host = "localhost",
            database = "ServerApi",
            user = "postgres",
            password = "123456zx" 
            )
            cursoring = connection.cursor()

            pg_select = """ SELECT COUNT(id) FROM public."request" """

            cursoring.execute(pg_select)
            request_count = cursoring.fetchone()
            connection.commit()
            
            return request_count

        except Exception as e :
            print(e)

        finally:
            if connection :
                cursoring.close()
                connection.close()
                

    def get_successful_request_count(self) :
        try :
            connection = psycopg2.connect(
            host = "localhost",
            database = "ServerApi",
            user = "postgres",
            password = "123456zx" 
            )
            cursoring = connection.cursor()

            pg_select = """ SELECT COUNT(id_response) FROM public."response" 
            WHERE city_name  != 'invalid' """

            cursoring.execute(pg_select)
            request_count = cursoring.fetchone()
            connection.commit()
            
            return request_count

        except Exception as e :
            print(e)

        finally:
            if connection :
                cursoring.close()
                connection.close()
                


    def get_all_response(self) :
        try :
            connection = psycopg2.connect(
            host = "localhost",
            database = "ServerApi",
            user = "postgres",
            password = "123456zx" 
            )
            
            cursoring = connection.cursor()

            pg_select = """ SELECT city_name FROM public."response"  """

            cursoring.execute(pg_select)
            request_count = cursoring.fetchall()
            connection.commit()
           
            lst_all_response = []
            for item in request_count:
                count_response_city = request_count.count(item)
                lst_all_response.append((item, count_response_city))

            return list(set(lst_all_response))

        except Exception as e :
            print(e)

        finally:
            if connection :
                cursoring.close()
                connection.close()
               




