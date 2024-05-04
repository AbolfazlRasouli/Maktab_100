def add(num1, num2: float) :
    return num1 + num2


def multipiy(num1, num2: float) :
    return num1 * num2


def subtract(num1, num2: float) :
    return num1 - num2

def division(num1, num2: float) :
    return num1 / num2


def operator(func: str, num1: float, num2: float) :
    match func:
        case 'add' :
            result = add(num1, num2)
        case 'multiply' :
            result = multipiy(num1, num2)
        case 'subtract' :
            result = subtract(num1, num2)
        case 'divide' :
            result = division(num1, num2)

    return result

while True :
    try : 
        a , b = map(float, input('Enter your number :  ').split())
        func = input('Enter your operator :')
        print(operator(func, a, b))
        break
    except Exception as e :
        print(e)
        print('Invalid . please try again.')