import pprint

student = [
    {'name' : 'John', 'age' : 20},
    {'name' : 'Alic', 'age' : 18},
    {'name' : 'Bob', 'age' : 22},
    {'name' : 'Emily', 'age' : 19}
]

list_sorted = sorted(student , key= lambda x : x['age'], reverse= True)
print(list_sorted)
for i in list_sorted :
    pprint.pprint(i)
