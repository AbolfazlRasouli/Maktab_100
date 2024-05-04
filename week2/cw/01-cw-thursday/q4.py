def add(num1, num2) :
    return num1 + num2

def multiply(num1, num2) :
    return num1 * num2

def subtract(num1, num2) :
    return num1 - num2

def divide(num1, num2) :
    try :
        return num1 / num2
    except ZeroDivisionError :
        print('number two can not zero')


while True :
    try :
        a , b = map(float , input('Enter your number').split())
        break
    except Exception as e :
        print(e)
        print('Invalid. Please try again')


print(f'add : {add(a , b)}')
print(f'multiply : {multiply(a , b)}')
print(f'subtract : {subtract(a , b)}')
print(f'divide : {divide(a , b)}')