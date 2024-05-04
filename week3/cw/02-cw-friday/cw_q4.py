string_list = ['apple', 'banana', 'orange', 'grape', 'kiwi']
print(string_list)
y = list(map(lambda x : x.upper(), string_list))
print(y)
x = list(filter(lambda z : 'A' not in z, y))
print(x)