class Employee:
    counter = 0

    def __init__(self, name, age, salary):
        self.name=name
        self.age=age
        self.salary=salary
        Employee.counter +=1

    def display(self):
        return "name: {}, age: {}, salary: {}".format(self.name, self.age, self.salary)

    def give_raise(self , amount):
        self.salary+= amount

    @staticmethod
    def give_raise_to_all(employees:list , amount):
        for emp in employees:
            emp.salary += amount
    
    @classmethod
    def get_counter(cls):
        return cls.counter
    
    @classmethod
    def average(cls, employees:list):
        total = 0
        for emp in employees:
            total += emp.salary
        return total/cls.counter
    
    # @staticmethod
    # def validate_name(employees:list ,name):
    #     for name in employees:
    #         if not name.isalpha():
    #             return "is not validate"
    #     return "is validate"

e1= Employee("ali", 30, 200)
e2= Employee("zeinab", 21, 500)

employees = [e1 , e2]

Employee.give_raise_to_all(employees, 200)
print(e1.salary)

print(Employee.average(employees))












# class Manager(Employee):
#     def __init__(self, name, age, salary, my_employee=None):
#         super().__init__(name, age, salary)
#         if my_employee is None:
#             self.my_employee=[]
#         else:
#             self.my_employee= my_employee
        
#     def add_emp(self, emp):
#         if emp not in self.my_employee:
#             self.my_employee.append(emp)











