# def funktsiya_nomi(param1,param2):
#   # funktsiya tanasi 
    # return natija
# def plus(a,b):
#     result = a + b
#     return result
    
# res = plus(5,6)
# print(res) # 11
# for i in range(1,11):
#     print(plus(1,i))

# print("hello world")


# def main(x,y):
#     return x + y

# main(1) # TypeError: main() missing 1 required positional argument: 'y'

# def main(x,y=0):
#     return x + y

# print(main(1)) # 1
# print(main(1,2)) # 3

# def main(x,y=0,z=0):
#     return x + y + z

# print(main(1)) # 1
# print(main(1,2)) # 3
# print(main(1,2,3)) # 6

# *args - arguments 
# def main(*args):
#     print(type(args)) #<class 'tuple'>
#     print(dir(args))
#     for i in args:
#         print(i)
#     return sum(args)

# x,*y = 1,2,3,4,5
# print(x,y)
# print(main(1,2,3,4,5)) # 15

# def main(*args):
#     for i in args:
#         print(i)

# main(True,1,1.2,[1,2,3], "str")

# **kwargs - keyword arguments
# def main(**kwargs):
#     print(type(kwargs)) # <class 'dict'>
#     print(dir(kwargs))
#     for i in kwargs:
#         print(i)

# main(a=1,b=2,c=3)

# super func 
# def main(*args,**kwargs):
#     print(args) # (1, 2, 3, 4, 5)
#     print(kwargs) # {'a': 1, 'b': 2}

# main(1,2,3,4,5,a=1,b=2)

# lambda - anonim function 
# l = lambda x,y : x + y
# print(l(1,2)) # 3

# filter , zip, sort, map 
# arr = list(range(1,11))

# print(list(filter(lambda x: x % 2 == 0, arr))) # [2, 4, 6, 8, 10]

# map 
# print(list(map(lambda x: x**2, arr))) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]    

# filter - berilgan ketmalik elementlarini berilgan funksiya natijasiga kora filterlaydi
# print(list(filter(lambda x:x>2,[1,2,3,4]))) # [3, 4]
# map - berilgan ketmalik elementlariga berilgan funksiyani har biri uchun qollaydi
# print(list(map(lambda x:x**2,[1,2,3]))) # [1, 4, 9]

# task 1
# Sonlar ro‘yxatidan juft sonlarni kvadratga oshirib, natijani qaytaring.
# numbers = [1, 2, 3, 4, 5, 6]
# Natija: [4, 16, 36]

# task 2 
# Berilgan ro‘yxatdagi barcha so‘zlarni katta harflarga o‘giring.
# words = ['hello', 'world', 'python']
# Natija: ['HELLO', 'WORLD', 'PYTHON']

# task 3 
# Ro‘yxatdagi faqat musbat sonlarni oling va ularning kubini hisoblang.
# numbers = [-3, 2, 4, -1, 5]
# Natija: [8, 64, 125]

# task 4 
# Ro'yxatdagi sonlarni juft bo'lsa ikkiga ko‘paytirib, toq bo'lsa chiqarib tashlang.
# numbers = [2, 3, 4, 5, 6]
# Natija: [4, 8, 12]

# task 5
# Ro'yxatdan barcha "Palindrom" bo'lgan sonlarni qoldiring.
# numbers = [121, 202, 345, 444, 567]
# Natija: [121, 202, 444] 

# task 6 
# Listdagi sozlarni belgilar soni boyicha saralang
# words = ['python', 'algorithm', 'map', 'function']
# Natija: ['map','python','function','algorithm',]

# def hello(func):
#     def inner():
#         print("Hello ")
#         func()
#     return inner

# def name():
#     print("Alice")
    
# obj = hello(name)
# obj()

# Dekoratorlar - bu bir funksiyani qabul qilib uni ishlashini o'zgartiruvchi boshqa bir funksiyalar hisoblanadi
# def decor(func):
#     def inner(*args):
#         if func(*args):
#             print("True")
#         else:
#             print("False")
#     return inner

# @decor 
# def main(a,b):
#     if a > b:
#         return True
#     else:
#         return False
        
# main(4,2)

# @decor
# def simple(x,y):
#     print(x + y)
# simple(1,2)


# numbers = [1, 2, 3, 4, 5, 6]
# print(list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers))))



# Fayl - Kompyuter xotirasida malum bir katakchalarni bir nom ostiga biriktirish
Papka - 
# Fayl formatlari ? fayllarni turlari 

# ozodbek.mp3 - audio 

# .exe - Windows uchun dastur
# .zip - Arxiv
# .txt - Matn
# .pdf - Matn,Rasm aralash formatlari
# .doc - Matn hujjatlar
# .xls - Excel
# .psd - Photoshop
# .ai - Illustrator
# .jpg - Rasm 
# .png - Fonsiz rasm 

# Win + R > diskmgmt.msc
# Win + R > %temp% > Enterni bosib ochilgan papka ichidagi hamma narsani o'chirib tashesiz
# CTRL + Alt + Del 