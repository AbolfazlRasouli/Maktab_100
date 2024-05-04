class Person :
    counter = 0
    

    def __init__(self , name : str , age : int, adderes :str):
        self.name = name
        self._age = age
        self.adderes = adderes
        Person.counter += 1
        self.id = Person.counter
       

       

    # def setter(self) :
    #     pass

    # def getter(self) :
    #     pass

    def introduce(self) :
        return f' My name is {self.name} I am  {self._age} I live in {self.adderes}'

    def change_adders(self, adderes) :
        self.adderes = adderes


    @classmethod
    def get_count(cls):
        return cls.counter
            

    def __str__(self) :
        return f' member of person : {Person.counter}' 


p = Person('abolfazl' , 28, 'tehran')
print(p.introduce())
p.change_adders('shiraz')
print(p.adderes)
print(p.id)

p2 = Person('ali' , 30 , 'tehran')
# print(p2.id)
# print(p.id)

print(p2._age)
# print(p2)
# print(Person.counter)
