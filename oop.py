# Obyekt:
#     sifati - qanday , qanaqa ? 
#     harakati - nima qiladi ?
# x = 10
# print(type(x)) # <class 'int'>

# s = "text"
# print(s)
# print(s.split())


# class Phone:
#     brand = "Samsung"
#     model = "A71"
    
#     battery = 2040
#     ram = 8
#     rom = 64
    
#     def call(self):
#         print("Call.")
    
#     def on(self):
#         print('Welcome')
    
#     def off(self):
#         pass

# print(Phone) # <class '__main__.Phone'>
# print(Phone.brand) #Samsung
# print(Phone.model) #A71

# class Phone:
    
#     def __init__(self,brand,model,battery,ram,rom):
#         self.brand = brand
#         self.model = model
#         self.battery = battery
#         self.ram = ram
#         self.rom = rom
    
#     def call(self):
#         print("Call.")
    
#     def on(self):
#         print('Welcome')
    
#     def off(self):
#         pass
    
# p1 = Phone("Apple","14 pro",3200,8,128)
# p2 = Phone("Apple","13 pro max",3000,8,256)

# print(p1.model) # 14 pro
# print(p2.model) # 13 pro max
# print(p1.call()) # Call.
# print(p2.on()) # Welcome

class Car:
    company = "Tesla"
    
    def main(self):
        pass

# print(hasattr(Car,"model")) # False
# setattr(Car,"model","Tesla X") # obyektga yangi sifat biriktirish
# print(hasattr(Car,"model")) # True
# print(Car.model) # Tesla X

# print(getattr(Car,"model")) # Tesla X

# try:
#     print(getattr(Car,"price")) # AttributeError
# except Exception as e:
#     print(e)
# print("continue...")

# delattr(Car,"model") #  model attr o'chirildi

# print(getattr(Car,"model")) # AttributeError: type object 'Car' has no attribute 'model'

print(dir(Car))