def my_rang(x, y, z = 1) :
    try :
        x = int(x) ; y = int(y) ; z = int(z)
    

        if z == 0 :
            raise Exception ('bbbbbbbbbbbbbbbbbbbbbbbbb')
        elif z > 0 and x < y:
            while x < y: 
                yield x
                x += z
        elif z < 0 and x > y :
            while x > y :
                yield x
                x += z
    except :
        print('x, y, z invalid')

for i in my_rang(10,1,-1) :
    print(i)





# for i in range(10, 0, -2) :
#     print(i)

# for i in range(1, 10) :
#     print(i)