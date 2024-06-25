import math
import random

# math - modul > matematik amallar uchun ishlatiladi 
# random - tasodifiy qiymatlar bilan ishlash uchun 

# int , float
# int - butun sonlar 

# abs - sonni modulini olish 
# -5 > 5
# 10 > -10
# negative > positive
# positive > negative 
# print(abs(-12)) # 12

# sum - berilgan ketma-ketlik sonlar yigindisini qaytaradi 

# print(sum([1,2,3])) # 6
# print(sum((1,2,3))) # 6

# print(sum(range(1,11))) # 55

# pow - berilgan sonni berilgan son darajasini qaytaradi 
# print(pow(2,2)) # 4
# print(pow(2,10)) # 1024

# print(min([1,2,3])) # 1
# print(max([1,2,3])) # 3

# print(math.pow(2,2)) # 4.0

# print(math.pi) # 3.141592653589793

# round() - sonlarni yaxlitlash uchun kerak 

# print(round(math.pi)) # 3
# print(round(math.pi,5)) # 3.14159
# print(round(math.pi,2)) # 3.14

# print(math.ceil(12.1)) # 13 > sonni qoldigi bolsa yuqoriga qarab yaxlitlash
# print(math.floor(12.99)) # 12 > sonni qoldigi bolsa pastga qarab yaxlitlash

# print(round(12.60)) # 13
# print(round(12.5)) # 12
# print(round(12.99)) # 13
# print(round(12.1)) # 12

# random 

# print(random.random()) # 0 bilan 1 orasidagi bitta tasodify sonni qaytaradi
# print(random.randint(1,10)) # berilgan 2 son orasidagi bitta tasodify sonni qaytaradi

# print(random.choice("python")) # berilgan ketma-ketlikdan bitta tasodify elementni  qaytaradi
# print(random.choice([1,2,3,4])) # berilgan ketma-ketlikdan bitta tasodify elementni  qaytaradi
# a = [1,2,3,4,5]
# random.shuffle(a) # berilgan ketma-ketlik elementlarini joylarini tasodify tarzda almashtirish
# print(a)

# berilgan ketma-ketlikdan korsatilgan miqdorda elementlarni olib massiv qilib qaytaradi 
# print(random.sample("Python programming language", 5))


# Password generator 
# numbers = "0123456789" # 0-9
# letters_low = "absdefjklmnoprstqufhyzxwvir" # a-z
# letters_up = letters_low.upper() # A-Z

# letters = numbers + letters_up + letters_low

# password_lenght = int(input("Parolda nechta belgi bo'lishi kerak ?"))

# if password_lenght > 6:
#     password = ""
#     for i in range(password_lenght):
#         random_letter = random.choice(letters)
#         password += random_letter
#     print(f"Sizning parolingiz : {password}")
# else:
#     print("Parol 6 ta belgidan kam bo'lishi mumkin emas !")