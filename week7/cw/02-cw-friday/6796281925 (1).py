# approach NO.1

# class Event:
#     def __init__(self, name, capacity) -> None:
#         self.name = name
#         self.date = ''
#         # ظرفیت
#         self.capacity = capacity
#         self.purchase_num = 0
#         # # ظرفیت باقیمانده
#         # self.remain_capacity = ""

#     def add_purchase_num(self, num):
#         self.purchase_num += num
#         self.purchase_num = self.purchase_num + num
    
#     def get_remain_capacity(self):
#         return self.capacity - self.purchase_num


# e1.add_purchase_num(5)
# print(e1.get_remain_capacity())
# e1.add_purchase_num(5)
# print(e1.get_remain_capacity())

# ==============================================

class Event:
    def __init__(self, name, capacity) -> None:
        self.name = name
        self.date = ''
        # ظرفیت
        self.capacity = capacity
        # # ظرفیت باقیمانده
        self.remain_capacity = capacity

    def change_remain_capacity(self, num):
        if self.remain_capacity >= num:
            self.remain_capacity -= num
        # self.remain_capacity = self.remain_capacity - num
    
    def get_remain_capacity(self):
        return self.remain_capacity
    
    # def __str__(self) -> str:
    #     return f"{self.name}, {self.capacity}, {self.remain_capacity}"
    
    def __str__(self) -> str:
        if self.capacity > 0 :
            return f"{self.name} :: remain capacity is : {self.remain_capacity}"
        return f"{self.name} :: No remain capacity"
        
   

e1 = Event('m_100', 20)

e1.change_remain_capacity(10)
print(e1.get_remain_capacity())
e1.change_remain_capacity(10)
print(e1.get_remain_capacity())

print(e1.name , f"remain capacity is : {e1.get_remain_capacity()}")

