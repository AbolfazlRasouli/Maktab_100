
class Cake:

    def init(self, flavor, size, price):

        self.flavor = flavor
        self.size = size
        self.price =price


    def describe(self):
        return f' your cake is {self.flavor}// and size :{self.size}// and price is :{self.price}'

cake1 =Cake("kakao", 200, 2000)
print(cake1.describe())