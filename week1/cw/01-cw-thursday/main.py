import random

# 01
# print('"Hello, world"')
# oldest = None
# youngest = None
# for item in range(3) :
#     age = int(input(f'Enter your age{item + 1} : '))
#     if oldest == None and youngest == None :
#         oldest = age
#         youngest = age
#     else :
#         if age > oldest :
#             oldest = age
#         elif age < youngest :
#             youngest = age
# print(oldest,youngest)

    


# 02
# num1 = int(input('Enter your number1 :'))
# num2 = int(input('Enter your number2 :'))
# print(f'sum : {num1+ num2}')
# print(f'difference : {num1- num2}')
# print(f'product : {num1* num2}')
# print(f'remainder : {num1% num2}')
# print(f'division : {num1// num2}')





# 03
# name = input('Enter your name :')
# last_name =input('Enter your last name :')
# age = int(input('Enter your age :'))
# print(f'"Hello {name} {last_name}, you are {age} years old."')




# 04
# pass1 = input('Enter your string :')
# lst = [False, False, False, False]

# if len(pass1) > 8 :
#     for up in pass1 :
#         if up.isupper() :
#             lst[0] = True
#         if up.islower() :
#             lst[1] = True
#         if up.isdigit() :
#             lst[2] : True
#         if not up.isalnum() :
#             lst[3] : True
    
#     if False in lst :
#         print('its week')
#     else :
#         print('its strong')
# else :
#         print('its week')







# 05
# ai_choice = random.randint(1, 20)
# print(ai_choice)
# user_input = int(input('Enter your guess :'))
# if ai_choice == user_input :
#     print('guess correct')
# elif ai_choice - user_input < 5 :
#     print('Too High')
# else :
#     print('Too Low')




# 06
# character1 = input("Enter your string1 :")
# character2 = input("Enter your string2 :") 
# separeted_cha1 = character1[:2]
# separeted_cha2 = character2[:2]
# print(separeted_cha2 + character1[-1] + " " + separeted_cha1 + character2[-1] )





# 07
# my_list = []
# for i in range(10) :
#     user_input = int(input('Enter'))
#     my_list.append(user_input)
# print(my_list)

# print(f'index 1 : {my_list[0]} and index -1 : {my_list[-1]}' )

# my_list.reverse()
# print(f'reverse : {my_list}')

# my_list.sort(reverse=True)
# print(f'sort : {my_list}')

# my_list.append(50)
# print(f'append : {my_list}')



# 08
# n = int(input("enter your number :"))
# for i in range(1, n + 1) :
#     for j in range(i) :
#         print(j + 1 , end=' ')
#     print()


# 09
# for i in range(1, 10) :
#     for j in range(1, 10) :
#         print(f'{i * j:3}', end=' ')
#     print()


# 10
# user = int(input('Enter'))
# my_list = []
# for i in range(user) :
#     user_input = int(input('Enter'))
#     my_list.append(user_input)
# print(my_list)

# list_even = []
# list_odd = []

# for i in my_list :
#     if i % 2 == 0 :
#         list_even.append(i)
#     else :
#         list_odd.append(i)

# print(f'list even : {list_even}')
# print(f'list odd :{list_odd}')



# 11
# my_list = []
# for i in range(5) :
#     user_input = int(input('Enter'))
#     my_list.append(user_input)
# print(my_list)

# sum_list =0
# for item in my_list :
#     sum_list += item
# print(f'avg : {sum_list / len(my_list)}')




# 12
word = input('Enter your string :')

# روش اول 
cou = 0
for char in word :
    if char == ' ' :
        continue
    cou += 1
print(cou)

# روش دوم
print('length : ', len(word.replace(' ','')))


print(f' reverse order : {word[::-1]}')

# روش اول 
word_list = word.split()
for letter in word_list :
    print(letter)

# روش دوم
[print(f'letters = {letters} len = {len(letters)}') for letters in word.split()]