import math 
import random

# print(math) # <module 'math' (built-in)>
# print(dir(math)) # barcha method va atributlarini ro'yhati
# print(math.pi) # 3.141592653589793

# high order functions 
# print() , len(), range() 

# print(round(3.2)) # 3
# print(round(3.6)) # 4

# print(round(math.pi,2)) # 3.14
# print(round(math.pi,3)) # 3.142


# print(math.ceil(7.1)) # 8
# print(math.floor(7.8)) # 7

# print(dir(random))
# name = "Python or Javascript"
# # tasodify 1 ta elementni olish
# print(random.choice(name)) 
# # siz ko'rsatgan ketma-ketlikdan siz korsatgan miqdorda tasodifiy elementlarni massiv ko'rinishida qaytaradi
# print(random.sample(name, 3)) 
# # 0 dan siz kiritgan songa qadar 1 ta tasodifiy sonni qayataradi
# print(random.randint(0,10))
# # siz kiritgan sonlar orasida 1 ta tasodifiy sonni qayataradi
# print(random.randrange(0,10)) 
# a = [1,2,3,4,5]
# random.shuffle(a)
# print(a) # berilgan massivni elementlarini tasodifiy qilib aralashtiradi

# task 1 
# user kiritgan son miqdorida belgilardan iborat parol hosil qiling (parolda albatta bitta katta harf, bitta son va maxsus belgi ishtirok etishi shart , parol uzunligi 6 ta dan kam bolmasligi kerak)
letters = "asdfghjklzxcvbnmqwertyuiop"
upper_letters = letters.upper()
nums = "0123456789"
symbols = "!@#$%^&*()_<>?"

to_password_data = letters + upper_letters + nums + symbols
password = ""
pass_length = int(input("Password len ?"))

if pass_length > 5:
    for i in range(pass_length):
        password += random.choice(to_password_data)
print(password)

print("".join(random.sample(to_password_data, pass_length)))
