import datetime

current_time = datetime.datetime.now()

name , birth_year = input("enter your name : ") , int(input("enter your Birth year : "))

current_year = current_time.year

age = current_year - birth_year

print(f' "Hello,{name}! You are {age} years old."')
print(' "Hello,{}! You are {} years old."'.format(name, age))
