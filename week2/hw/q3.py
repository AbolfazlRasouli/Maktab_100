# 3
user_str = input('Enter your string : ')
letters = 0
digit = 0
for chr in user_str :
    if chr.isalpha() :
        letters += 1
    elif chr.isdigit() :
        digit += 1
print(f'Letters : {letters}')
print(f'Digits : {digit}')