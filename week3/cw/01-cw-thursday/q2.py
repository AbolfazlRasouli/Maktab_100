my_str = input('Enter your str :').strip().split()
count_number = 0
lst = []
for item in my_str :
    if my_str.count(item) == 1 :
        lst.append(item)
        count_number += 1

print(' '.join(lst))
print(count_number)