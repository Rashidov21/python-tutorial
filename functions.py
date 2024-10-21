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

