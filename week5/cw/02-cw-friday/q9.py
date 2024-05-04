class Student :
    def __init__(self, age : list, height : list, weight : list):
        self.age = age
        self.height = height
        self.weight = weight

    def average_weight(self) :
        self.weight = list(map(float, self.weight))
        return round(sum(self.weight) / len(self.weight), 2)
    
    def average_height(self) :
        return round(sum(self.height) / len(self.height), 2)
    
    def average_age(self) :
        return round(sum(self.age) / len(self.age), 2)

# milk
class A(Student) : 
    def __init__(self, age : list, height : list, weight : list):
        super().__init__(age, height, weight)

class B(Student) :
    def __init__(self, age : list, height : list, weight : list):
        super().__init__(age, height, weight)


flag = True
while flag :
    try :
        ageA = list(map(int, input('Enter A ages : ').split()))
        heightA = list(map(float, input('Enter A Height : ').split()))
        weightA = list(map(float, input('Enter A Weight : ').split()))

        ageB = list(map(int, input('Enter B ages : ').split()))
        heightB = list(map(float, input('Enter B Height : ').split()))
        weightB = list(map(float, input('Enter B Weight : ').split()))

        flag = False
    except :
        print('Invalid value. try again')

studentA = A(ageA, heightA, weightA)
studentB = A(ageB, heightB, weightB)

if studentA.average_height() > studentB.average_height() :
    print('class A is taller : {}'.format(studentA.average_height)) 
elif studentA.average_height() < studentB.average_height() :
    print('class A is taller : {}'.format(studentB.average_height)) 
else :
    if studentA.average_weight < studentB.average_weight :
        print('same height , but class A has lower weight : {}'.format(studentA.average_weight))
    elif studentA.average_weight > studentB.average_weight :
        print('same height , but class B has lower weight : {}'.format(studentB.average_weight))
    else : 
        print('same')