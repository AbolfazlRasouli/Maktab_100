def fibo(n: int) :
    if n == 0 or n == 1 :
        return 1
    else :
        return fibo(n - 1) + fibo(n - 2)


n = int(input('Enter : '))
for i in range(n) :
    print(fibo(i) , end = ' ')