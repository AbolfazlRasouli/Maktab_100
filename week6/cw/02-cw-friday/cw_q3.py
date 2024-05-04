
class Employee:
    
    def __init__(self, name:str, salary:float):
        self.__name=name
        self.__salary=salary
    
    # @property
    # def get_name(self):
    #     return self.__name


    def get_name(self):
        return self.__name
    
    def get_salary(self):
        return self.__salary
    
    
    # @get_name.setter
    # def set_name(self, new_name):
    #     self.__name = new_name
    
    def set_name(self,new_name):
        self.__name = new_name
    
    def set_salary(self,new_salary):
        self.__salary = new_salary
    
    
        
        
        
e1=Employee("John Doe", 5000.0)
print(e1.get_name())
print(e1.get_salary())

e1.set_name("Jin mammad")
e1.set_salary(1000)
print(e1.get_name())
print(e1.get_salary())

print(e1._Employee__name)
print(e1.__name)
print(e1.__salary)
