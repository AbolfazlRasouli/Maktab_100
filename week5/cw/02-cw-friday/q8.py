# from colorama import Fore, Back, Style

class Shape:
    def __init__(self,name:str, color:str):
        self.name=name
        self.color=color
    
    def display_name(self):
        return "Shape_name: {}".format(self.name)
    
    def display_color(self):
        return "Shape_color: {}".format(self.color)
    
    
class Rectangle(Shape):
    def __init__(self, name:str, color:str, length:int, width:int):
        super().__init__(name, color)
        self.width = width
        self.length = length

    def area(self):
        return self.length *self.width
    
    def perimeter(self):
        return 2*(self.length+self.width)
    
    def Return(self):
        return self.color

rec1=Rectangle("Rectangle","RED",10,3)

print(rec1.display_name())
print(rec1.display_color())
# print(Fore.(rec1.Return()) + rec1.display_color())
print(rec1.area())
print(rec1.perimeter())
# print(Fore.RED + 'some red text'+ Fore.WHITE)
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')    
