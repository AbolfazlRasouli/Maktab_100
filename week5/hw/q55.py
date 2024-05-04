class Employee:
    total_count = 0

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        Employee.total_count += 1

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.salary}")

    def give_raise(self, amount):
        self.salary += amount

    @classmethod
    def give_raise_to_all(cls, amount):
        cls.total_count = 0
        for employee in employees:
            employee.give_raise(amount)
            cls.total_count += 1

    @classmethod
    def average_salary(cls):
        total_salary = sum(employee.salary for employee in employees)
        return total_salary / cls.total_count

    @staticmethod
    def validate_name(name):
        return len(name.split()) == 2
    

employees = [
    Employee("John Doe", 25, 50000),
    Employee("Jane Smith", 30, 60000),
    Employee("Mike Johnson", 35, 70000)
]