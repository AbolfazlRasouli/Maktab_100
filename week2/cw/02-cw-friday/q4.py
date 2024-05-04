import random 
import string 
 
 
def mypassword(length: int): 
    lowercase = string.ascii_lowercase 
    uppercase = string.ascii_uppercase 
    digits = string.digits 
    special = string.punctuation 
    min_length = 8 
    min_lowercase = 1 
    min_uppercase = 1 
    min_digits = 1 
    min_special = 1 
    total_chars = min_lowercase + min_uppercase + min_digits + min_special 
    length = max(length, total_chars, min_length) 
    # این پرانترز برای این که ما برای کد ها انتر زدیم تا بیفته خط پایین . 
    #  جون در یه خط نوشتن خیلی طولانی ش می کرد . و پایتون میگه برای این کار پرانترز بذار یا اسلش  بذار . 
    password = ( 
            random.choices(lowercase, k=min_lowercase) + 
            random.choices(uppercase, k=min_uppercase) + 
            random.choices(digits, k=min_digits) + 
            random.choices(special, k=min_special) + 
            random.choices((lowercase + uppercase + digits + special), k=length - total_chars) 
    ) 
    random.shuffle(password) 
    return password 
 
 
print("".join(mypassword(int(input(">")))))