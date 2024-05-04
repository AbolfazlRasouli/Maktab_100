my_dict = {'name' : 'kelly',
           'age' : 25,
           'salary' : 8000,
           'city' : 'new york'}

def city_location(my_dict) :
    y = my_dict['city']
    # my_dict.pop('city')
    del my_dict['city']
    # my_dict['location'] = y
    my_dict.update({'location' : y})
    return my_dict

print(city_location(my_dict))