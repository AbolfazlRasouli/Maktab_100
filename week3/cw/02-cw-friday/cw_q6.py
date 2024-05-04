def fibonacci_generatore(number) :
    f1 = 0
    f2 = 1
    for _ in range(number) :
        yield f1
        f1 , f2 = f2 , f1 + f2


for _ in fibonacci_generatore(5) :
    print(_ , end=' ') 
