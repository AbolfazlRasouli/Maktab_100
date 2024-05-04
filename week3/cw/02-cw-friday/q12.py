def converted(celcius) :
    farenhait = list(map(lambda x : x * 9/5 + 32 , celcius))
    return farenhait

celcius = [12,34,23,56,42,16,32]
print(converted(celcius))