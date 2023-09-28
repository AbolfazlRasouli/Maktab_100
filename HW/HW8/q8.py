import requests
import pprint


url="https://my-json-server.typicode.com/typicode/demo/posts"
global_var = None


def get_request() :
    try:
        response = requests.get(url)
    except Exception as e :
        print('e')  
    if response.status_code == 200 :
        data = response.json()
        return data  
    else :
        return 'not found'



def process_data(result) :
    
    mylist_id = []
    mylist_title = []
    
    for mydict in result :
        num = 0
        for  _, value in mydict.items():
            if num == 0 :
                mylist_id.append(value)
            else :
                mylist_title.append(value)
            num += 1

    return mylist_id , mylist_title
        

def local_func(local_var1, local_var2):

    len_local_var1 = 0
    len_local_var2 = 0

    def nonlocal_func():
        nonlocal len_local_var1
        nonlocal len_local_var2
        len_local_var1 = len(local_var1)
        len_local_var2 = len(local_var2)
         
    nonlocal_func()
    global_var = len_local_var1 + len_local_var2
    return global_var
        
        
        



    


result = get_request()    
pprint.pprint(result)
var_id , var_title = process_data(result)
print(local_func(var_id, var_title))