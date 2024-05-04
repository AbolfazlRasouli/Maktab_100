def my_prime(number) :
    for i in range(2, number //2 + 1) :
        if number % i == 0 :
            return True
        
    # return [True for i in range(2, number //2 + 1) if number % i == 0]



def generate_prime(start, end):
    # روش اول 
    # return [x for x in range(start, end+1) if all(x%y!=0 for y in range(2,x))]
    # return [x  if all(x%y!=0 for y in range(2,x))]
    # for x in range(start, end+1)
    

    # روش دوم
    # not my_prime(i)  : اگر true برگردونه میکنه false به خاطر not
    # از طرفی if شرط من باید true باشه تا اجازه بدم بری داخل بدنه 
    # پس اگر تابع به من True بده . اون رومیکنه false و اینطوری if اجرا نمیشه
    return [i for i in range(start, end + 1) if i > 1 and not my_prime(i)]

    




start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
result = generate_prime(start, end)
print(result)