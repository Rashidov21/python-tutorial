# for , while 
# for - sanoqli takrorlanish 
# while - to'xtovsiz takrorlanish 

# for i in "python":
#     print(i)

# range() - sonlar oralig'i , diapazon
# range(start,stop,step)
# print(list(range(5,11,2))) # [5 , 7 , 9]
# print(list(range(5))) # [0,1,2,3,4]

# for i in range(1,11):
#     print(i)
# else: # takrorlanish so'ngida nimadur ish qilish uchun else bloki
#     print("for tugadi")

# s = 0
# for i in range(1,6):
#     s += i 
# else:
#     print(s**2) # 225

# for x in range(10):print(x, end="") # 0123456789


# WHILE 

# i = 0
# while True: # to'xtovsiz takrorlanish
#     i+=1
#     print("While loop ", i)

# i = 50
# while i > 0:
#     i -= 1
#     print(i)
# i = 0
# while  i < 100:
#     i += 1
#     if i % 2 == 0:
#         continue # juft sonlar takrorlanishi bajarilmaydi, keyingi siklga o'tiladi
#     if i == 71:
#         break # sikl to'xtaydi
#     print(i)

# k = 5
# n = int(input("N ?"))
# if n > 0:
#     for i in range(n):
#         print(k)

# task 10
# n = 7
# s = 1
# for i in range(2,n+1):
#     s += 1 / i 
# print(s) # 2.5928571428571425

# task 11
# n = 5
# s = n ** 2
# for i in range(2 * n**2):
#     s += (n+1)**2
# print(s)


# task 1
# berilgan str dan raqamlar , harflar va maxsus belgilarni alohida qilib ekranga saralab chiqaruvchi dastur tuzing
# input : a = "1a$2o&"
# output : "ao" , "12", "$&"

# nums = ""
# alpha = ""
# symbols = ""

# input_data = "1a$2o&"

# for i in input_data:
#     if i in "asdfghjklqwertyuiopzxcvbnm":
#         alpha += i 
#     if i in "0123456789":
#         nums += i 
#     if i in "!@#$%^&*()<>?{}[]":
#         symbols += i 
# print(nums,alpha,symbols) # 12 ao $&
       