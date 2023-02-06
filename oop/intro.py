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
class Home:
    """Home object"""
   
    def __init__(self,color,rooms,price):
        self.color = color
        self.rooms = rooms
        self.price = price

    def get_info(self):
        print(self.color)
        print(self.rooms)
        print(self.price)
        
        
home_1 = Home("white",3,15000)
home_2 = Home("red",5,5000)
home_3 = Home("yellow",4,15000)

print(getattr(home_1,"color")) # white
setattr(home_1,"windows", 4)
print(hasattr(home_1,"color")) # true
print(getattr(home_1, "windows")) # 4
delattr(home_1, "color") # delete color attr
# print(getattr(home_1,"color")) # AttributeError
