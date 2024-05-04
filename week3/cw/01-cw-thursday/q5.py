with open('text.txt', 'r+') as myfile :
    reader = myfile.read().replace('.', '').split()

    result = list(filter(lambda x : x != 'and' and x != 'is' and x != 'the', reader))

    print(reader, '/n' , result)

    my_dict = {}
    for word in result :
        counter = result.count(word)
        my_dict.setdefault(word, counter)
    
    res = sorted(my_dict.items() , key= lambda x :(x[1], x[0]), reverse= True)
    print(res)
    for i in range(5) :
        print(f'{res[i][0]} - {res[i][1]} occurance')