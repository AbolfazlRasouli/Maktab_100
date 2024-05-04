def divide_chunks(my_list : list ) :
    for item in range(0, len(my_list), 3):
        yield my_list[item : item + 3]

def rever(lst : list) :
    for i in lst :
        i.reverse()
        yield i

my_list = [1,2,3,4,5,6,7,8,9]
mini_list = list(divide_chunks(my_list))
print(mini_list)
lst_rever = list(rever(mini_list))
for i in lst_rever :
    print(i)
