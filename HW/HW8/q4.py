import requests 
from bs4 import BeautifulSoup
import pprint



url = "https://my-json-server.typicode.com/horizon-code-academy/fake-movies-api/movies"
url_jason = "https://my-json-server.typicode.com/typicode/demo/posts"
def get_req() :
    try :
        responsive = requests.get(url)
        # print(responsive)
    except Exception as e :
        print(e)
    if responsive.status_code == 200 :
        movie_list = responsive.json()
        # pprint.pprint(movie_list)
        return movie_list
    

def user_input():
    
    title = input('Enter the title movie')
    year = input('Enter the year movie')
    runtime = input('Enter the runtime movie')
    poster = input('Enter the poster movie')
    data = {
        'id': 6,
        'Title': title,
        'Year' : year,
        'Runtime' : runtime,
        'Poster' : poster
    }
    return data

def post_movie() :
    data = user_input()
    # data = {
    #     "id": 4,
    #     "title": "Post 4"
    # }
    response = requests.post(url, data= data)
    print(response.status_code)




# movie_list = get_req()
# for movie in movie_list :
#     print(f"Title : {movie['Title']} , year : {movie['Year']}")

post_movie()








# روش دوم
# def get_req(myurl, somthing_to_search):
#     if somthing_to_search:
#         RESPONSE = req.get(url=myurl, params=somthing_to_search)
#     else:
#         RESPONSE = req.get(url=myurl)
        
#     data = BeautifulSoup(RESPONSE.content, 'html.parser')
#     return data
#     # return API.json()
    
# def post_req(myurl, myjson):
#     RESPONSE = req.post(myurl, json = myjson)
#     data = BeautifulSoup(RESPONSE.content, 'html.parser')
    
#     print(data)
#     print(RESPONSE.status_code)

# def delete_req(myurl, somthing_to_delete):
#     RESPONSE = req.delete(url=myurl, params=somthing_to_delete)
#     data = BeautifulSoup(RESPONSE.content, 'html.parser')
    
#     print(data)
#     print(RESPONSE.status_code)