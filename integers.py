# int() 1.2 >> 1
# print(int("1") + 2) 
# float() >> 1 >> 1.0
# print(float("1.2") + 1.2)
# print(float(1) + 1.2) # 2.2

# # bin 
# print(bin(10)) # 0b1010
# print(oct(10)) # 0o12
# print(hex(10)) # 0xa

# print(round(12.2)) # 12
# print(round(12.6)) # 13
# print(abs(-12)) # 12
# print(pow(2,6)) # 64 >> 2 ** 6
# print(max([1,2,3])) # 3
# print(min([1,2,3])) # 1
# print(sum([1,2,3])) # 6

n = 10.0
n1 = 10.3
print(n.is_integer()) # True
print(n1.is_integer()) # False

# variant 1 
# import math
# print(math.pi)  # 3.141592653589793
# # variant 2
# from math import pi 
# print(pi) # 3.141592653589793
# import math 

# print(math.ceil(12.6)) # 13
# print(round(12.6)) # 13
# print(math.floor(12.6)) # 12

# import random

# print(round(random.random() * 4)) # 0 va kiritilgan son orasidagi tasodify son
# print(random.randint(0,10)) # 2 ta  sonni orasidagi tasodify son

# print(random.choice("python")) # ketma-ketlikdan tasodify bitta elementni olish
# print(random.sample("python", 2)) # ketma-ketlikdan tasodify bir nechta elementni olish
# arr = [1,2,3,4,5]
# random.shuffle(arr)# berilgan massiv elementlarini indexlarini qorishtrish
# print(arr) 

# task 1 
# user ikita son kiritadi birinchi kiritgan soni bu hosil qilinishi kerak bolgan parollar soni 
# ikkinchi kiritgan soni bu parollarda belgilar ni maksimal soni 
# user sonlarni kiritishi bilan u hohlagancha parollarni hosil qilib bering 


# task 2 
# "yangi o'zbekiston" so'zida "svet" so'zidagi belgilar necha marta duch kelishi mumkinligini 
# hisoblovchi dastur tuzing


# task 3
# 100 marta takrorlanadigan kodda nechi marta foydalanuvchi kiritgan son duch kelganini toping; (kod 100 marta takrorlanadi user son kiritgan boladi  0 <  userNum < 100 ; random shaklida olingan takrorklanishdagi son user ni soniga togri kelsa shart bajarilgan demak; nechi marta userni soni togri kelganini chiqaring)

# task 4
# foydalannuvchi kiritgan sonlar orasida barcha sonlarni konsolga chiqaring

# task 5
# foydalannuvchi kiritgan sonlar orasida barcha sonlarni konsolga chiqaring
# kiritgan sonlari ham qo'shilib chiqadi ushbu sonlar yigindisi va ularning
# kvadrati yigindilarini ham hisoblang