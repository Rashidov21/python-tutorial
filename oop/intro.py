# x = 10
# print(type(x)) # <class 'int'>

# class Home:
#     color = "white"
#     rooms = 4
#     price = 25000
    
#     def open_the_door(self):
#         print("Open, door.")
    
#     def close_the_window(self):
#         print("Close , window.")
    
# home_1 = Home()
# home_2 = Home()
# home_3 = Home()

# home_3.color = "red"

# print(home_1)
# print(home_2)
# print(home_3.color) # red

# home_1.open_the_door() #Open, door.
# print(home_1.color)
# home_2.close_the_window() #Close , window.
# print(home_2.price)

# class Car:
#     """Main Car object"""
#     pass
# class UserProfileTemplateView:
#     pass 

# uptv = UserProfileTemplateView()
# def init(color, rooms=None, price=0):
#     color = color
#     rooms = rooms 
#     price = price
    
    
# init()
# class Home:
#     """Home object"""
   
#     def __init__(self,color,rooms,price):
#         self.color = color
#         self.rooms = rooms
#         self.price = price

#     def get_info(self):
#         print(self.color)
#         print(self.rooms)
#         print(self.price)
        
        
# home_1 = Home("white",3,15000)
# home_2 = Home("red",5,5000)
# home_3 = Home("yellow",4,15000)

# print(getattr(home_1,"color")) # white
# setattr(home_1,"windows", 4)
# print(hasattr(home_1,"color")) # true
# print(getattr(home_1, "windows")) # 4
# delattr(home_1, "color") # delete color attr
# print(getattr(home_1,"color")) # AttributeError


# OPP 
# 1-inkapsulyatsiya
# 2-meros olish 
# 3-polimorfizm


# 1-inkapsulyatsiya
    # 1-private 
    # 2-protect
    
# class Bank:
#     # cash = 1300
#     web_money = 560
    
#     _cash = 1500 # private 
#     __cash = 1800 # protect
    
#     def pay(self, payment_method, money):
#         if payment_method == "cash":
#             self.cash - money
#             print(f"Bank cash : {self.cash}")
#         elif payment_method == "web":
#             self.web_money - money
#             print(f"Bank web money : {self.web_money}")
#         else:
#             print("Payment method is not support !")           
            
#     def check_balance(self):
#         print(f"Bank cash : {self.cash}")
#         print(f"Bank web money : {self.web_money}")
        
#     def __getattribute__(self):
#         return Bank.__cash
  

# b.cash = 0 # cash is 0

# b.check_balance()
# b._cash = 0
# b.__cash = 0
# print(b.cash)      
# print(b._cash)      
# print(b.__getattribute__)  

# __getattr__, __setattr__ и __delattr__. 

# 2- meros olish 

# class Person:
#     def __init__(self,name,gender):
#         self.name = name
#         self.gender = gender
#         print("Person object create")
        
        
#     @staticmethod  
#     def class_method():
#         print("class Person")
        

# class Teacher(Person):
#     def __init__(self,name,gender,subject, salary):        
#         self.subject = subject
#         self.salary = salary 
#         return super().__init__(name,gender)
        
#     def info(self):
#         print(f"Teacher : {self.name}\n{self.gender}\n{self.salary}")
    
#     @staticmethod  
#     def class_method():
#         print("class Teacher")

# class Student:
#     def __init__(self,name,gender,age):
#         self.name = name
#         self.gender = gender
#         self.age = age
            
#     def info(self):
#         print(f"Student : {self.name}\n{self.gender}\n{self.age}")
    
#     @staticmethod  
#     def class_method():
#         print("class Student")


# t = Teacher("John", "male", "Chemical", 1500)
# t.info()
# s = Student("Mike", "male", 14)
# p.class_method()
# t.class_method()
# s.class_method()

class Red:
    value = 0
        

class Green:
    value = 0

class Blue:
    value = 0
        
class RGB(Red,Green,Blue):
    
    def __init__(self, v1,v2,v3):
        RGB.__bases__[0].value = v1
        RGB.__bases__[1].value = v2
        RGB.__bases__[2].value = v3
       
        print("RGB model is created")

    def generate_color(self):
        color = []
        for i in RGB.__bases__:
            color.append(i.value)
        return tuple(color )  
        # return (self.red_value,self.green_value,self.blue_value)
    
rgb = RGB(23,20,48)
print(rgb.generate_color())
