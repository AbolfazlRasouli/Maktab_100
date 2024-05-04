tuple_list = [('Hello', 'world'), ('open', 'AI'), ('GPT', '3')]

# روش خودم
x = list(map(lambda y : y[0] + " " + y[1], tuple_list ))
print(x)
# روش گروهی
print(list(map(lambda y : ''.join(y), tuple_list)))
