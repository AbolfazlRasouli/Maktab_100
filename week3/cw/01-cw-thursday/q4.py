# روش اول
# def dict_counter(lst) :
#     my_dict = {}
#     for item in lst :
#         counter = lst.count(item)
#         my_dict[item] = {'count' : counter}

#     return my_dict

# # 1
# # برای گرفتن ورودی
# my_str = input('Enter sentence :').split('.')
# my_lst = ' '.join(my_str).split()

# # 2
# lst = []
# while True :
#     inp = input('Enter :')
#     if inp == 'done' :
#         break
#     lst.append(inp)
    

# print(dict_counter(my_lst))





# روش دوم
# method setdefult(key , value)
def dict_counter(lst) :
    my_dict = {}
    for item in lst :
        counter = lst.count(item)
        my_dict.setdefault(item, {'count': counter})

    return my_dict

# 1
# برای گرفتن ورودی
my_str = input('Enter sentence :').split('.')
my_lst = ' '.join(my_str).split()

# 2
# lst = []
# while True :
#     inp = input('Enter :')
#     if inp == 'done' :
#         break
#     lst.append(inp)

print(dict_counter(my_lst))