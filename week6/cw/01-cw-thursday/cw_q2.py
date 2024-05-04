class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price}"


class ShoppingCart:
    def __init__(self):
        self.items = []

    def __str__(self):
        print(f'{self.items}')
        return ' '.join(str(item) for item in self.items)


    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items

    def __add__(self, other):
        lst = []
        lst =  self.items + other.items
        print(lst)
        for i in lst :
            print(str(i)) 

     

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def total_price(self):
        return sum(item.price for item in self.items)
    




item1 = Item("samsung", 10)
item2 = Item("iphone", 20)
item3 = Item("apple", 50)


cart1 = ShoppingCart()
cart1.add_item(item1)
cart1.add_item(item2)

cart2 = ShoppingCart()
cart2.add_item(item3)

print(cart1) 
print(cart2)  

# print(len(cart1))  
# print(item1 in cart1)  
# print(item2 in cart2)  

# cart1 + cart2 


# cart1.remove_item(item2)
# print(cart1) 

# print(cart1.total_price())  
# print(cart2.total_price())  




