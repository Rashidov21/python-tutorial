# l = list()
# l = []
for i in dir(list()):
    print(i)
# list - tartibli elmentlar ketma-ketligi (ro'yhat) > RAM da yonma-yon katakchalarda ma'lumot saqlash usuli
# a = [1,2,3,4,5]
# for i in a:
#     print(i)

# print(list("python")) # ['p', 'y', 't', 'h', 'o', 'n']
# print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for i in list(range(10)):
#     print(i)

# a, *b = [1,2,3,4,5]
# print(a)
# print(b)

# arr = list(range(5))
# print(len(arr)) # 5
# print(arr[0])
# print(arr[-1])


# list methods 

# arr = list(range(5))
# print(arr[1:3]) # [1, 2]

# arr = [True,1,1.2,"str",[1,2,3]]
# arr = [
#   [1, 2, 3],
#   [4, -5, 6],
#   [7, 8, 9]
# ]
# for i in arr:
#     for k in i:
#         print(k)

# s = "python"
# s[0] = "j" # TypeError: 'str' object does not support item assignment

# arr = [1,2,3]
# arr[0] = 0
# print(arr) #[0, 2, 3]

# arr = [1,2,3]
# arr = list(range(1,11))
# print(arr) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list generator 
# a = []
# a.append(1) # listni oxiriga element qoshish
# a.append(2) # listni oxiriga element qoshish
# a.append(3) # listni oxiriga element qoshish
# print(a) # [1, 2, 3]

# task 1 
# 1 dan 20 gacha bolgan sonlar ichida faqat 3 ga qoldiqsiz bolinadiganlaridan iborat massiv hosil qiling 

# arr = []
# for i in range(1,21):
#     if i % 3 == 0:
#         arr.append(i)
# print(arr) # [3, 6, 9, 12, 15, 18]

# print([i for i in range(1,21) if i % 3 == 0]) # [3, 6, 9, 12, 15, 18]
# print([i ** 2 for i in range(1,21) if i % 3 == 0]) #  [9, 36, 81, 144, 225, 324]

# arr = [[1, 2], [3, 4], [5, 6]]
# arr = [j * 10 for i in arr for j in i if j % 2 == 0 ]
# print(arr) # [20, 40, 60]

# function - kod bo'lagi 
# def main(x):
#     return x ** 2

# print(main(2)) # 4

# map , zip , filter 

# map - siz ko'rsatgan funktsiyani siz ko'rsatgan ketma-ketlik elementlarini barchasiga qo'llaydi 

# res = map(main,[1,2,3,4,5])
# print(res) # <map object at 0x000001A204569960>
# print(type(res)) # <class 'map'>
# print(dir(res)) # ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

# def main(x):
#     return x ** 2
# res = map(main,[1,2,3,4,5])
# print(list(res)) # [1, 4, 9, 16, 25]

# zip - berilgan ketma-ketliklardan baravariga element olib yangi ketma-ketlik sifatida qaytaradi
# print(zip("abc",[1,2,3])) # <zip object at 0x000002A9D5C83A00>
# print(list(zip("abc",[1,2,3]))) # [('a', 1), ('b', 2), ('c', 3)]
# print(list(zip("abc",[1,2,3],"python"))) #  [('a', 1, 'p'), ('b', 2, 'y'), ('c', 3, 't')]

# filter - berilgan funktsiya natijasiga ko'ra ketma-ketlik elementlarini filterlaydi 
# def main(num):
#     if num % 2 == 0:
#         return num

# print(filter(main, [1,2,3,4,5])) # <filter object at 0x0000019946479B40>
# print(list(filter(main, [1,2,3,4,5]))) # [2, 4]

# print(list(filter(lambda x : x > 5, list(range(15))))) # [6, 7, 8, 9, 10, 11, 12, 13, 14]

# append - massiv oxiriga element qoshish
# arr = [1,2,3]
# arr.extend([4,5,6]) # massivni boshqa bir massiv bilan kengaytirish
# print(arr) # [1, 2, 3, 4, 5, 6]
# arr = [1,2,3] 
# arr.insert(0,"vahaha") # massivga korsatilgan indexga korsatilgan elementni qoshish
# print(arr) # ['vahaha', 1, 2, 3]
# arr = [1,2,3] 
# a = arr.pop(0) # korsatilgan elementni ochirish
# print(a) # 1
# print(arr ) # [2, 3]
# arr = [1,2,3] 
# # del arr[1]
# # print(arr) # [1, 3]

# arr.remove(3) # berilgan elementni massiv ichidan o'chirish
# print(arr) # [1, 2]

# arr.clear() # masivni butunlay tozalash
# print(arr) # []

# arr = ["salom", "qale", "ishlar"]
# print(arr.index("qale")) # 1 - massivda siz korsatgan elementni indexini olish

# arr = [1,2,3,1,4,5,1,1] 
# print(arr.count(1)) # berilgan elementni massiv ichida nechi marta ishtirok etganini topish

# arr = [1,2,3] 
# arr.reverse()
# print(arr) # [3, 2, 1]

# all - agar massiv ichida barcha elementlar boleanda True bo'lsa True qaytaradi aks holda False
# arr = [1,2,3] 
# print(all(arr)) # True
# arr = [0,1,2,3] 
# print(all(arr)) # False
 
# any - agar massiv ichida biror bir element boleanda True bo'lsa True qaytaradi aks holda False
# arr = [0, False,"",[]]
# print(any(arr)) # False
# arr = [1, False,"",[]]
# print(any(arr)) # True

# arr = [0,4,5,6,3,4,1,5,6]
# # arr.sort()
# # arr.sort(reverse=True)
# print(arr) # [6, 6, 5, 5, 4, 4, 3, 1, 0]
# arr = ["Print","PRINT","print"]
# arr.sort(key=str.upper, reverse=True)
# print(arr) # 

# sorted - ketma-ketlik elemetnlarini saralash uchun alohida metod 
# arr = [1,4,5,7,8,9,6,3,2,45,65]
# print(sorted(arr)) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 45, 65]
# print(sorted(arr, reverse=True)) #[65, 45, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# arr = ["Print","PRINT","print"]
# print(sorted(arr,key=str.lower))
 
 
# l = list(range(10))

# tuple - 
# t = tuple("python")
# t = ()
# print(type(t)) # <class 'tuple'>
# print(dir(t)) # 
