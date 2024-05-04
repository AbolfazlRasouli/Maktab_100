class Animals :

    counter_animmal = 0
    species = {}

    def __init__(self, name, age) :
        self.name = name
        self.age = age

    @classmethod
    def get_counter_animal(cls) :
        return cls.counter_animmal
    
    def valiator_age(self) :
        try :
            if self.age < 0 :
                raise Exception(' INvalid age')
        except Exception as e :
            print(e)
            self.name = 'new_name'
            self.age = 0

    def display(self) :
        return f'animal name is :{self.name} and age is : {self.age}'

    @staticmethod
    def get_species_count(key_species) :
        Animals.species[key_species] = Animals.species.get(key_species, 0) + 1
        return Animals.species
    
obj1 = Animals('katty' , 20)
obj2 = Animals('roky' , 20)
obj3 = Animals('jessi' , -20)

# obj1.valiator_age()
# obj2.valiator_age()
obj3.valiator_age()
print(obj3.name)
# print(obj3.age)


obj1.get_species_count('gorbeh')
obj3.get_species_count('sag')
print(obj2.get_species_count('gorbeh'))
