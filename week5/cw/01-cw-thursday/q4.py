class SmartPhone:
    def __init__(self, brand:str, storage:int, ram:int, camera:int):
        self.brand=brand
        self.storage=storage
        self.ram=ram
        self.camera=camera
    
    def display(self):
        return 'My mobile phone brand is {brand}\nstorage:{}\nram:{}\ncamera:{camera}'.format(self.storage,self.ram,camera=self.camera,brand=self.brand)
        
    
mob1=SmartPhone("samsung",128,8,64)
print(mob1.display())