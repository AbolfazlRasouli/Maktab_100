# 1
while True :
    try :
        user_input = int(input('Enter your number :'))
        break
    except :
        print('Invalid number. Please try again')

def division(num) :
    count_division = 0
    for item in range(1, num) :
        if num % item == 0 :
            count_division += item
    if count_division == num :
        return f'{num} : yes'
    else :
        return f'{num} : no'
# 6 496 8128
print(division(user_input))

















# lst = [10,11,1,2,4,5,4,6,3,2]
# print(sum([10,11,1,2,4,5,4,6,3,2]))


# for i in range(10,1,-1) :
#     print(i)

# x = 'A'
# lst = ['a' , 'b' , 'c']
# print(x.lower() in lst)
    
    
    
# st = 'ABCSDEW'
# x = 'a'
# print(x.upper() in st)