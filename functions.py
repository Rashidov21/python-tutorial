# def func_name(arguments):
    # function block 
    # return 
    
# def main(x):
#     pass # hech qanday amal yo'q

# class Main:
#     pass 

# for i in range(10):
#     pass

# def func():
#     print("func")
#     return "func 1"
#     # print("func")

# print(func) # <function func at 0x0000017565E061F0>
# print(func()) #  func 1

# def check_user(username): # postional argument
#     print(username)

# check_user("mahatma") # mahatma

# def check_user(username=None): # not postional argument
#     print(username)
     
# check_user() # None


# def user_data(name, age, salary, address):
#     data =[name, age, salary, address]
#     for item in data:
#         print(item)

# user_data("John",30,1500,"Oklohoma")


# def user_data(*args):
#     for item in args:
#         print(item)
 
# user_data("John",30,1500,"Oklohoma")

# *args - arguments
# b , *a = 1,2,3,4
# print(b)  # 1
# print(a)  # [2, 3, 4]

# **kwargs 
# d= dict(name="john", age=30)
# print(d) #{'name': 'john', 'age': 30}
# def func_kwargs(**kwargs):
#     print(type(kwargs))#<class 'dict'>
#     print(kwargs) # {'name': 'john', 'age': 30}

# func_kwargs(name="john", age=30)


# def super_func(*args, **kwargs):
#     for i in args:
#         print(i)
#     for i in kwargs.items():
#         print(i)

# super_func(1,"str", True, name="john", age=30)

# def summa(x,y):
#     return x + y

# print(summa(1,2)) # 3


# def main():
#     print(10)
    
# print(main) # <function main at 0x000001FE856261F0>

# main = lambda x : x + 10

# print(main(10)) # 20

# arr = [1,47,6,9,7,56,20,31,45,36,3,65,1,2,39,5,63,3,5,65,69]

# a = list(filter(lambda x : x > 30, arr))
# print(a) # [47, 56, 31, 45, 36, 65, 39, 63, 65, 69]


# res = lambda x,y,z: x+y+z
# print(res(1,2,3)) # 6

# def func(x, у):
#     for i in range(1, x+1):
#         yield i ** у

# print(func(5, 2)) # generator object
# print(list(func(5, 2))) # [1, 4, 9, 16, 25]


# def check_int_value(f):
#     print(x, y)
#     # print(f)
#     # print(dir(f))
#     # print(type(f))
#     # print("Function : summa()") 
#     return f 

# @check_int_value
# def summa(x, y):
#     return x + y

# print(summa(1,2)) #3
# from benchmark import benchmark

# @benchmark
# def fetch_webpage():
#     import requests
#     webpage = requests.get('https://google.com')

# # fetch_webpage()


# @benchmark
# def count_zeros(num):
#     count = 0
#     for i in range(1, num):
#         if i % 10 == 0:
#             count = count + 1
 

# count_zeros(10000000)

# import math 
# print(math.factorial(5)) # 120


# def factor(n):
#     if n == 0 or n == 1: 
#         return 1 
#     else:
#         return n * factor(n - 1) 