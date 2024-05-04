
customers = {}

def add_item(name, product_name, price, count):
    
    if name not in customers:
        customers[name] = {}
    
    # افزودن محصول به سبد خرید مشتری
    if product_name in customers[name]:
        # اگر محصول قبلاً در سبد خرید بود، تعداد آن را قزاز می‌دهیم
        customers[name][product_name]['count'] = count
    else:
        # اگر محصول جدیدی بود، آن را به سبد خرید اضافه می‌کنیم
        customers[name][product_name] = {'price': price, 'count': count}
    return f"product : {product_name}  price : {price} and count  {count} cart shopping {name} added."






def remove_item(name, product_name):
    # بررسی وجود مشتری
    if name not in customers:
        raise Exception("The  customer was not found.")
    
    # بررسی وجود محصول در سبد خرید مشتری
    if product_name in customers[name]:
        del customers[name][product_name]
        return f"product {product_name} cart shopping {name} delet."
    else:
        return f"product {product_name}  cart shopping {name} not found ."





def calculate_total(name):
    # بررسی وجود مشتری
    if name not in customers:
        raise Exception("The  customer was not found.")
    
    
    total_price = 0
    for product_name, product_info in customers[name].items():
        total_price += product_info['price'] * product_info['count']
    
    return total_price


def show_cart(name):
    # بررسی وجود مشتری
    if name not in customers:
        raise Exception("The  customer was not found.")
    
    print(f"cart shopping {name} : {customers[name]}")
    




while True:
    print("Meno :")
    print("1. Add product to cart")
    print("2. Remove product to cart")
    print("3. Calculat total price of the shopping cart")
    print("4. show shopping cart")
    print("5. exit")
    
    choice = input("Enter your number of meno : ")
    print('-' * 50)
    
    if choice == '1':
        name = input("Enter name : ")
        product_name = input("Enter name product : ")
        price = float(input("Enter price : "))
        count = int(input("Enter count : "))
        print(add_item(name, product_name, price, count))
        print('-' * 50)



    elif choice == '2':
        name = input("Enter name : ")
        product_name = input("Enter name product : ")
        try :
            print(remove_item(name, product_name))
        except Exception as e :
            print(f"Error: {e}")
        print('-' * 50)



    elif choice == '3':
        name = input("Enter name : ")
        try:
            total_price = calculate_total(name)
            print(f"The total price of the shopping cart  {name}: {total_price}")
        except Exception as e:
            print(f"Error: {e}")
        print('-' * 50)
        


    elif choice == '4':
        name = input("Enter name : ")
        try:
            show_cart(name)
        except Exception as e:
            print(f"Error: {e}")
        print('-' * 50)
        

    elif choice == '5':
        break

    else:
        print("Please select a valid number from the menu.")





  
