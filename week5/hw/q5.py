import timeit
import time
from functools import wraps




def cache(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = (*args, *kwargs.items())
        if key in cache:
            print("aaaaa")
            return cache[key]
        else :
            result = func(*args, **kwargs)
            cache[key] = result

        return result
    
    

    return wrapper



def timer_process(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        with open("log.txt", "a") as f:
            f.write(f"{func.__name__}  {execution_time} ")
        return result
    return wrapper






@timer_process
@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)




@timer_process
@cache
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


# print(fibonacci(50))
print(fibonacci(8))

# print(factorial(50))
print(factorial(8))
























# def cache(func):

#     dict_cache = {}
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         key = args + tuple(kwargs.items())
#         if key in dict_cache:
#             return dict_cache[key]
#         else :
#             result = func(*args, **kwargs)
#             dict_cache[key] = result
#             return result
#     print(dict_cache)

#     return wrapper




# def timer_process(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         start_time = timeit.default_timer()
#         with open("log.txt", "w") as f:
#             f.write(f"{start_time} ")
#         return start_time
#     return wrapper
