my_list = input('Enter your string and number :').split(',')
print(my_list)

count_letter = 0
count_float = 0
couunt_int = 0

# روش اول
for item in my_list :
    try: 
        a = float(item)
        if int(a) == a :
            couunt_int += 1
        else :
            count_float += 1
    except :
        count_letter += 1
print(f'int : {couunt_int}')
print(f'float : {count_float}')
print(f'letters : {count_letter}')



# روش دوم : روش مربی 
for value in my_list:
    if value.isdigit():
        couunt_int += 1
    elif value.replace(".", "").isdigit():
        count_float += 1
    else:
        count_letter += 1
print(f'int : {couunt_int}')
print(f'float : {count_float}')
print(f'letters : {count_letter}')



