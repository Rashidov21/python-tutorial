# Dasturlash tili -  tarjimon 
# Interpretator - ona tili o'qituvchisi
# Kompilyator -  tarjimon dastur

# Variables 

# variable - RAM xotira katakchasiga olib boruvchi yol

# 1. ingliz tilida 
# 2. mantiqan to'g'ri , kichik harflar bilan 
# 3. birinchi belgisi raqam bo'lishi mumkin emas 
# 4. harflar , sonlar va _ dan boshqa belgi mumkin emas 
#  5. zaxiralangan so'zlar bilan variable ochish mumkin emas

# import keyword
# print(keyword.kwlist)

# _ = 1
# _for = 10
# print(_for * 2) # 20

# l  = [_ for _ in range(5)]
# print(l) # [0, 1, 2, 3, 4]
# f1 = "Michael Shumacher"

# uh = 1.80
# user_height = 1.80
# userHeight = 1.80
# USER_HEIGHT = 1.80
# print(USER_HEIGHT + 2)# 3.8
# x = 1

# Data Type - ma'lumot turi , xotira katakchasida saqlash mumkin bo'lgan ma'lumot birligi 

# 1. bool - True , False 
# 2. None - None 
# 3. int - 1, -1
# 4. float  - 1.0, -1.0
# 5. complex - 2n 
# 6. str - "s", 's' , """s"""
# 7. bytes  
# 8. bytearray

# Data Structure - xotira katakchasida saqlash mumkin bo'lgan ma'lumotlar tuzilmasi 

# 1. list - []
# 2. tuple  - ()
# 3. dict  - {}
# 4. set - {}
# 5. frozenset - frozenset()
# 6. range - range(10)

# function , type , module , ellipsis 


# print(2+2) # 4
# print(2-2) # 0
# print(4/2) # 2.0
# print(4//2) # 2
# print(7%3) # 1
# print(7*2) # 14
# print(3**2) # 9 

# print(2 * 2 / (3 + 1.5)) # 0.8888888888888888
# print(2 * 2 // (3 + 1.5)) # 0.0

# in - ichida , mavjudlikga tekshirish operatori 
# print("s" in "salom") # True
# print("s" in "xayr") # False

# not - emas , inkor operatori 
# print(not True) # False 
# print(not 0) # True
# print(not 1) # False

# print("s" not in "xayr") # True
# variant 1 
# x = 5
# x += 5
# print(x) # 10
# # variant 2 
# x = 5
# x = x + 5
# print(x) # 10


# print(2 == 2) # True
# print(1 != 2) # True
# print(1 > 0) # True
# print(1 < 0) # False 

# x = 1
# y = 1 
# z = 0
# print(x + y) # 2

# print(x is z) # False
# print(x is y) # True
# print(x is not z) # True

# and - mantiqiy VA 
# print("p" and 1 and -6 and 1) # 1
# or - mantiqiy YOKI 
# print(0 or "1" or -6 or -1) # 1

# 27, 24, 25, 26, 22, 21
# task 21
# x=int(input('X>>'))
# y=int(input('Y>>'))

# if x==0 and y==0:
#     print(0)
# elif x==0:
#     print(1)
# elif y==0:
#     print(2)
# else:
#     print(3)

# task 22
# x=int(input('X>>'))
# y=int(input('Y>>'))

# if x>0 and y>0:
#     print(1)
# elif x<0 and y>0:
#     print(2)
# elif x<0 and y<0:
#     print(3)
# else:
#     print(4)


# task 24
# x=int(input('X>>'))
# f=0
# if x>0:
#     f=2*sin(x)
# else:
#     f=x-6
# print(f)
