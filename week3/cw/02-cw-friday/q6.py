lst = []
while True :
    input_name = input("enter your name film : ")
    if input_name == 'done' :
        break
    year = input("enter your release year film : ")

    lst.append((input_name, year))

lst.sort(key= lambda x : (x[1], x[0]), reverse= True)
print(lst)