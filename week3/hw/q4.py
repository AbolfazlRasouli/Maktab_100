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
        return 'ZeroDivisionError : number2 can not zero'


while True :
    try :
        num1 , num2 = map(float , input('Enter your number1 and number2 : ').split())
        break
    except Exception as e :
        print(e)
        print('Invalid. Please try again')




operator = input("Enter your operator (+ or - or / or *) : ")
list_operator = ['+', '-', '*', '/']
if operator in list_operator :
    if operator == '+':
        result = add(num1, num2) 

    elif operator == '-':
        result = subtract(num1, num2)
        
    elif operator == '*': 
        result = multiply(num1, num2)
        
    elif operator == '/':
        result = divide(num1, num2)
                
else :
    print('Error : input operator is invalid')
    exit()

print(f'{num1} {operator} {num2} = {result}')


























# print(f'add : {add(a , b)}')
# print(f'multiply : {multiply(a , b)}')
# print(f'subtract : {subtract(a , b)}')
# print(f'divide : {divide(a , b)}')