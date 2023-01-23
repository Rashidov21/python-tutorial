# import keyword
# print(keyword.kwlist)

# l = list()
# l = [1,"number",[1,2,3]]
# print(l[0]) # 1
# print(len(l)) # 3

# l.append("append element")
# print(l) #[1, 'number', [1, 2, 3], 'append element']
# append - oxiriga qoshish
# pop - oxiridan o'chirish 
# index - element indexini olish 
# insert - index oraqali element qoshish
# reverse - elementlar indexini teskari qilish
# count - list da elementni takrorlanishini sanash 
# sort - saralash 
# remove - elementni ochirish
# extend - boshqa massiv bilan kengaytirish
# copy - list nusxasini olish 
# del l[index] - element ochirish 
# clear - listni tozalash

# x,y = 1,2
# print(x+ y) # 3

# x,y,*z = [1,2,3,4,5,6]
# print(x,y,z)
# print(type(z)) # class list

# *args -  , **kwargs 

# def check_user(*args):
#     for i in args:
#         print(i)
        
# check_user("dskjskj", 12, True, 'adagbd')

# arr = [1,2,3,4,5]
# print(arr[:]) # [1,2,3,4,5]
# print(arr[3:]) # [4,5]
# print(arr[2:3])# [3]
# arr.reverse() #[5, 4, 3, 2, 1]
# print(arr)
# arr = [1,2,3,4,5]

# arr = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

# for lists in arr:
#     for i in lists:
#         print(i)
# print([x for i in arr for x in i]) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# task 1 
# user kiritgan so'zni birinchi harfini oxirgi harfi bilan almashtiring
# masalan : qovun >> novuq
# s = "qovun"
# print(list(s)[0])
# print(list(s)[-1])
# l = list(s) #['q', 'o', 'v', 'u', 'n']
# last_item = l[-1] # oxirgi elementni vaqtinchalik olish
# l[-1] = l[0]
# l[0] = last_item
# print("".join(l))

# print(f"{s[-1]}{s[1:-1]}{s[0]}")


# l = list(range(10))

# print(l) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print([x for i in arr for x in i]) # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# arr = [1,2,3,4,5]
# # l = [i**2 for i in arr]
# # print(l) #[1, 4, 9, 16, 25]
# l = [i**2 for i in arr if i % 2 == 1]
# print(l) #[1, 9, 25]

# arr = [[1, 2], [3, 4], [5, 6]]
# new_аrr = [j * 10 for i in arr for j in i if j % 2 == 0 ]
# print(new_аrr) # [20, 40, 60]

# task 3
# user string kiritadi siz ichidan faqat "a" harflarini list generator 
# orqali yangi massivga yozing


# def main(num):
#     return num + 5

# arr = [1,2,3,4,5]

# print(map(main, arr)) #<map object at 0x0000012517E47460>
# print(list(map(main, arr))) # [6, 7, 8, 9, 10]

# name = "John"
# positons = [1,2,3,4]

# print(zip(name,positons)) # <zip object at 0x000002229F2E2B40>
# print(list(zip(name,positons))) # [('J', 1), ('o', 2), ('h', 3), ('n', 4)]

# for x in list(zip(name,positons)):
#     for i in x:
#         print(i , end="") # J1o2h3n4
        
# alpha = "abcdefgh"
# print(list(zip(alpha, list(range(len(alpha))))))
# # [('a', 0), ('b', 1), ('c', 2), ('d', 3), ('e', 4), ('f', 5), ('g', 6), ('h', 7)]
# letters = list(zip(alpha, list(range(len(alpha)))))
# e = "e"

# for i in letters:
#     if e == i[0]:
#         print(i[1])

# a = "aaaaa"
# b = list(range(10))
# print(list(zip(a,b))) # [('a', 0), ('a', 1), ('a', 2), ('a', 3), ('a', 4)]

# def odd(n):
#     if n % 2 == 1:
#         return n

# arr = list(range(1,11))



# print(list(filter(odd, arr))) # [1, 3, 5, 7, 9]

# task 4
# ikita sonlardan iborat massiv berilgan ularni ichidan takrorlanuvchi sonlarni oçhirib yuborin

# a = [1,2,3,6,4]
# b = [7,1,5,9,3]

# c = [7,2,5,9,6,4]