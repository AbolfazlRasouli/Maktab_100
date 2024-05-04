import random
import string


class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def change_password(self, new_password):
        self.password = new_password

    def reset_password(self):
        text_lower = string.ascii_lowercase + string.ascii_uppercase + string.digits
        self.password = "".join(random.choices(text_lower, k=5))

    def change_username(self, new_username):
        self.username = new_username


class Staff(User):
    id = 0

    def __init__(self, username, password, department, salary, tax):
        super().__init__(username, password)
        Staff.id += 1
        self.department = department
        self.validate_salary(salary)
        self.salary = salary
        self.validate_tax(tax)
        self.tax = tax
        self.staff_id = Staff.id

    def display_info(self):
        return f'username is: {self.username} and department is : {self.department} and salary is: {self.salary}.' \
               f'and tax is : {self.tax}'

    def validate_salary(self, salary):
        if not isinstance(salary, (float, int)) or salary <= 0:
            raise ValueError("invalid salary")


    def validate_tax(self, tax):
        if not isinstance(tax, (float, int)) or tax < 0:
            raise ValueError("invalid tax")
        else:
            return f'isvalid tax : {tax}'

    def change_salary(self, new_salary):
        self.salary = new_salary
    def calculate_net_salary(self):
        if self.tax > self.salary:
            return f'tax is bigger than salary'
        return self.salary - self.tax


class Student(User):
    id = 0
    academic_year = 1

    def __init__(self, username, password, major):
        # Student.id += 1
        super().__init__(username, password)
        self.major = major
        self.student_id = self.generatt_id()

    def display_info(self):
        return f'username is: {self.username} and major is : {self.major}'

    def change_major(self, new_major):
        self.major = new_major

    @classmethod
    def update_academic_year(cls):
        cls.academic_year += 1

    def generatt_id(self):
        my_id = string.digits
        return random.choices(my_id, k=5)


class Teacher(Staff):
    id = 0

    def __init__(self, username, password, department, salary, tax, subject):
        super().__init__(username, password, department, salary, tax)
        Teacher.id += 1
        self.subject = subject
        self.teacher_id = Teacher.id

    def display_info(self):
        return f'username is: {self.username} and department is : {self.department} and salary is: {self.salary}.' \
               f'and tax is : {self.tax} and subject is : {self.subject}'

    def change_subject(self, new_subject):
        self.subject = new_subject


class Course:
    id = 0

    def __init__(self, course_name):
        Course.id += 1
        self.course_name = course_name
        self.teachers = []
        self.students = []
        self.course_id = Course.id

    def add_student(self, item: Student):
        self.students.append(item)

    def remove_student(self, item: Student):
        if item in self.students:
            self.students.remove(item)
        else:
            return f'student is not exist'

    def clear_student(self):
        self.students = []

    def get_student(self):
        # for i in self.students:
        #     print(i.username)
        return self.students

    def set_teacher(self, new_teacher):
        self.teachers.append(new_teacher)

    def display_info(self):

        my_teachers = ' '.join(str(item.username) for item in self.teachers)
        my_students = ' '.join(str(item.username) for item in self.students)
        return f'courseid : {self.course_id}, and coursename : {self.course_name}, and teachers : ' \
               f'{my_teachers}, and students : {my_students}'


teacher1 = Teacher("meysam", 123, "riaziat", 2000, 400, "riazi")
teacher2 = Teacher("mamad", 456, "shimiat", 3000, 600, "olom")
student1 = Student("ali", 789, "engenering")
student2 = Student("asghar", 136, "chemistry")

course1 = Course("maktab")
course1.add_student(student1)
course1.add_student(student2)
course1.set_teacher(teacher1)
course1.set_teacher(teacher2)
print(course1.display_info())

