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