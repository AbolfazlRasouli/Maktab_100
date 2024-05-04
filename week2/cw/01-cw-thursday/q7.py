def add(num1, num2) :
    try :
        num1 = float(num1)
        num2 = float(num2)
        return num1 + num2
    except :
        raise TypeError("Both arguments must be numeric")

def multiply(num1, num2) :
    try:
        return num1 * num2
    except TypeError:
        raise TypeError("Both arguments must be numeric")

def subtract(num1, num2) :
    try:
        return num1 - num2
    except TypeError:
        raise TypeError("Both arguments must be numeric")

def divide(num1, num2) :
    try:
        return num1 / num2
    except TypeError:
        raise TypeError("Both arguments must be numeric")
    except ZeroDivisionError:
        raise ValueError("Division by zero is not allowed")


# while True :
#     try :
#         a , b = map(float , input('Enter your number').split())
    #     break
    # except Exception as e :
    #     print(e)
    #     print('Invalid. Please try again')

a = input('Enter your number')
b = input('Enter your number')
print(f'add : {add(a , b)}')
# print(f'multiply : {multiply(a , b)}')
# print(f'subtract : {subtract(a , b)}')
# print(f'divide : {divide(a , b)}')