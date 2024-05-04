class Circle :
    
    pi = 3.141

    def __init__(self, r) :
        self.r = r

    # qotr
    def calc_diameter(self) :
        return self.r * 2
    
  

    # دسترسی به pi از خود کلاس circle
    def calc_area(self) :
        return Circle.pi * (self.r ** 2)
    
    # mohit
    def calc_circumferece(self) :
        return 2 * self.pi * self.r
    

    def area_feet(self):
        return self.calc_area() * 10.7639
    
    def radius_from (self) :
        return self.calc_circumferece() // (2 * Circle.pi)

    def info_circle(self) :
        return f' area :{self.calc_area()} and circumferece : {self.calc_circumferece()} and diameter :{self.calc_diameter()} and radius_from :{self.radius_from()} '

while True :
    try :
        user_input = float(input("Enter your number : "))
        break
    except TypeError as e  :
        print('Invali number . please Try again.')


circle1 = Circle(user_input)
print(circle1.calc_area())
print(circle1.calc_diameter())
print(circle1.calc_circumferece())
print(circle1.radius_from())
print(circle1.area_feet())
print(circle1.info_circle())

