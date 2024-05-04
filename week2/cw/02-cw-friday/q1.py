def avg (list_number : list) :
    ''' Type arguman : list
     return avg , type  '''
    avg = sum(list_number) / len(list_number)
    return avg, type(avg)


a , b  = avg([1,2,3,4])  
print(a, b)

# assert avg([1,2,3,4]) , 'Exception Error '