# 5
n, m = map(int, input('Enter m and n members :').split())

list_z = []
list_a = []
list_b = []

for _ in range(n) :
    user_input = int(input('Enter your number for list-z :'))
    list_z.append(user_input)

for _ in range(m) :
    user_input = int(input('Enter your number for list-a :'))
    list_a.append(user_input)

for _ in range(m) :
    user_input = int(input('Enter your number for list-b :'))
    list_b.append(user_input)    

print(list_z)
print(list_a)
print(list_b)

happiness_level = 0

for item in list_z :
    if item in list_a :
        happiness_level += 1
    if item in list_b :
        happiness_level -= 1

print(f'happiness_level : {happiness_level}')
