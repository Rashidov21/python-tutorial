# list - tartibli elementlar ketma-ketligi

# list() , [] 
# print(list("python")) # ['p', 'y', 't', 'h', 'o', 'n']
# print(list("python","dddd")) # TypeError: list expected at most 1 argument, got 2

# arr = [1,2,3,4,5]
# print(arr[0]) # birinchi element
# print(arr[len(arr)-1]) # oxirgi element
# print(arr[-1]) # oxirgi element

# print(arr[3]) # 4
# print(arr[-2]) # 4

# arr = [1,2,3,4,5]
# arr[0] = 0
# print(arr) # [0, 2, 3, 4, 5]
# s = "strong"
# s[3] = "i"
# print(s) # TypeError: 'str' object does not support item assignment

# a,b,c = 1,2,3
# print(a+b+c) # 6

# x,y,z = [1,2,3,4,5,6,7,8,9,10] # ValueError: too many values to unpack (expected 3)
# x,y,*z = [1,2,3,4,5,6,7,8,9,10] # 
# print(x) # 1
# print(y) # 2
# print(z) # [3, 4, 5, 6, 7, 8, 9, 10]

# print(len([1,2,3])) # 3

# string = ["Python", "better", "very", "nice", "programming", "language"]
# # print(string[1::2]) # ['better', 'nice', 'language']
# # # print(string[-1]) # language
# # print(string[4:]) # ['programming', 'language']
# # print(string[1:2]) # ['better']
# print(string[::-1])  # ['language', 'programming', 'nice', 'very', 'better', 'Python']

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# l = [x * 2 for x in range(10)]
# lg = [i for i in range(10) if i % 2 == 0]
# print(lg)
# l = []
# for x in range(10):
#     l.append(x * 2)
    
# print(l) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

text = '''
Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''
# matnda har bir qatorda 5 ta belgidan kop bolgan so'zlardan iborat massiv tuzing 

# List Genarators

# l = []
# for i in range(10):
#     if i % 2 == 0:
#         l.append(i)
# print(l) # [0, 2, 4, 6, 8]


# print([i for i in range(10) if i % 2 == 0]) # [0, 2, 4, 6, 8]

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print([x for i in  matrix for x in i]) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
 
# l = []
# for x in matrix:
#     for i in x:
#         l.append(i)
# print(l)# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# arr = []
# arr.append(0) # bitta element qoshish uchun
# arr.extend([1,2]) # yangi massiv qoshish uchun 
# # arr[5] = 3 # IndexError: list assignment index out of range
# arr[0] = 1 # massivda mavjud elementni o'zgartirish
# # arr[10] = 20 # IndexError: list assignment index out of range
# arr.insert(0,5)
# arr.insert(10,5) # [5, 1, 1, 2, 5] # siz korsatgan index ga siz korsatgan elementni qoshadi

# arr = [1,2,3,4]
# arr.pop(0)  # siz korsatgan indexdan elementi ochiradi 
# arr.pop()  # agar index berilmasa oxirgi elementni ochiradi
# print(arr) # [2, 3]

# arr = [1,2,3,4]
# # del arr[0]
# # print(arr) # [2, 3, 4]
# del arr[:2]
# arr.clear() # massivni tozalaydi
# arr_2 = arr.copy() # massivni nusxalaydi
# print(arr) # []


# arr = list("python")
# p = "p" if "p" in arr else "not found"
# print(p) # p

# arr = [1,2,3]
# print(1 in arr) # True
# print(1 not in arr) # False

# arr = list(range(1,11))
# for i in arr:
#     if i == 7:
#         print("yes")

# print("bor" if 7 in list(range(1,11)) else "yoq")

# arr = list(range(1,11))

# print(arr.index(7)) # elementni indexini olish
# print(arr.count(7)) # elementni massiv ichida necha marta bor ekanini qaytaradi

# print(max(arr)) # 10
# print(min(arr)) # 1

# arr = [1,2,4,6,4,9,5,1,8,7]
# print(max(arr)) # 9
# print(min(arr)) # 1
# arr.sort()
# print(arr[len(arr)//2]) # 5

# arr = [0,1,True]
# print(any(arr)) # agar massiv ichida 1 dona bolsa ham Boleanda True qiymatga ega element bolsa TRue qaytaradi aks holda False qaytaradi

# print(all(arr)) # agar massiv ichida hamma elementlar Boleanda True qiymatga ega bolsa True qayataradi aks holda False
# arr = [0,1,True]
# arr.reverse() # massivni teskari qiladi
# print(arr) # [True, 1, 0]

# task 1
# 1 dan 50 gacha bolgan sonlardan iborat massiv hosil qiling , har 10 ta elementni alohida alohida massivlarga yozuvchi dastur tuzing

# task 2
# input : arr = ["s",1,True,False,2]
# output: [['s'],[True,False],[1,2]]


# if type(i) == bool:
# import random 

# arr = [1,2,4,6,4,9,5,1,8,7]
# print(random.choice(arr)) # tasodify 1 ta element
# random.shuffle(arr) # elementlarni joylashuvini aralashtirish
# print(arr) 
# arr_2 = random.sample(arr, 3) # tasodify 3 ta elementdan iborat massiv hosil qiladi
# print(arr_2) 

# arr = [5,6,4,982,3,54,498,6,2,26,4,33]
# # arr.sort()
# # print(arr) # [2, 3, 4, 4, 5, 6, 6, 26, 33, 54, 498, 982]
# arr.sort(reverse=True)
# print(arr) # [982, 498, 54, 33, 26, 6, 6, 5, 4, 4, 3, 2]

# sorted() - berilgan ketma ketlikni saralaydi
# for i in sorted([2,5,4,9,6,3],reverse=True):
#     print(i, end="") # 965432

# a = list(range(11))


# tuple - ozgarmas elementlar ketma-ketligi
# t = tuple() 
# t = ()
# t = (1,2,3)
# t[0] = 0 # TypeError: 'tuple' object does not support item assignment

# for i in tuple("tuple"):
#     print(i)

# set - unikal elementlar to'plami 
# s = {}
# s = set()
# s = set("assalom")
# print(s) # {'s', 'o', 'l', 'a', 'm'}

# united_set = set("pyt").union({'h','o','n'}) 
# print(united_set) # birlashgan 2 ta set

# united_set.update("1")
# print(united_set)

# set_a = set("python123")
# set_b = set("python")
# print(set_a.difference(set_b)) # ikita set ni farqini korsatadi


# dict - lug'at , elementlariga indeks orqali emas balki kalit so'z orqali murojaat qilinadigan elementlar to'plami

# d_1 = dict(a=10,b=20)

# print(d_1.keys()) # dict keys dict_keys(['a', 'b'])
# print(d_1.items()) # dict items tuple object dict_items([('a', 10), ('b', 20)])
# print(d_1.values()) # dict values  dict_values([10, 20])
 
# print(d_1["a"]) # 10
# print(d_1["b"]) # 20
# print(d_1["a"] + d_1["b"]) # 30

# # print(d_1["some_key"]) # KeyError: 'some_key'
# print(d_1.get("some_key")) # None

# d_2 = {
#     'name':'John',
#     'surname':'Doe',
# }
# d = dict(a=10,b=20)

# print('a' in d) # True - kalitni mavjudlikga tekshirish
# print(20 not in d) # True

# d.pop("a")
# print(d) # {'b': 20}
# d.popitem() 
# print(d) # 
# d.clear()
# print(d) # {}

# l = [0,False]
# print(any(l)) # birorta true bormi ?
# print(all(l)) # hammasi true mi ?

# d = dict(a=10,b=20)
# d.update({'c':30})
# d.update(d=40)
# print(d)  # {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# d = {}
# d.get() - kalit orqali qiymatni olish
# d.pop() - kalit orqali o'chirish 
# d.setdefault() - kalit orqali qiymat qoshish yoki olish
# d.items() -  dict elementlari kortej korinishida
# d.keys() -   dict kalitlari 
# d.values() - dict qiymatlari
# d.fromkeys() -  dict kalitlari
# d.clear() -  dict ni tozalash
# d.popitem() - tasodify elementni o'chirish
# d.copy() -  dict ni nusxalash