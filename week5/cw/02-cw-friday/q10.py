class Person:
    def __init__(self, name, age, address):
        self.name= name
        self.age = age
        self.address = address
    
class Student(Person):
    def __init__(self, name, age, address, email, Student_id):
        self.email = email
        self.student_id = Student_id
        super().__init__(name, age, address)

    def change_email(self, new_email):
        self.email = new_email
    
    def display(self):
        return "name: {} , age: {} , email: {} , address: {} , id: {}".format(self.name,self.age, self.email, self.address, self.student_id)

class Teacher(Person):
    def __init__(self, name, age, address, subject, teacher_id):
        self.subject = subject
        self.teacher_id = teacher_id
        super().__init__(name, age, address)

    def change_subject(self, new_subject):
        self.subject = new_subject
    
    def display(self):
        return "name: {} , age: {} , subject: {} , address: {} , id: {}".format(self.name,self.age, self.subject, self.address, self.teacher_id)

std1 = Student("zeinab", 21, "tehran","zzzzz@gmail.com", 123456)
teach1 = Teacher("mahsan", 26, "tehran","it", 987654)

print(std1.display())
print(teach1.display())

std1.change_email("aaaa@gmail.com")
teach1.change_subject("computer")

print(std1.email)
print(teach1.subject)

    