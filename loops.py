# Loops 
# for , while 
# while - toxtovsiz sikl 
# for - sanoqli sikl 

# for sikli - ketma-ketliklar bilan ishlaydi 
# for i in "python":
#     print(i)

# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# for i in range(1,6):
#     print(i)
    
# print(type(range(1,6)))
# print(dir(range(1,6)))

# range - 'start', 'step', 'stop'
# start = 1
# step = 3
# stop = 15
# for i in range(start, stop, step):
#     print(i)
# print(list(range(start, stop, step))) # [1, 4, 7, 10, 13]

# for x in range(10):
#     print(x)
    
# for k in "stars":
#     print(type(k)) 
#     print(k + "s")

# for i in input():
#     if i == "a":
#         print("yes")
    
# def main(num):
#     return num ** num

# for x in range(10):print(main(x))
# enumerate - element va  uni indexini olish uchun ishlatiladi 
# s = "Python is n1"
# for i in enumerate(s):
#     print(i) #(0, 'P')

# for i in range(5):
#     if i % 2 == 0:
#         print(i)
# else: # sikl tugasa biron ish qilish buchun else blokidan foydalaning
#     print("loop tugadi")

# i = 0

# while True:
#     i += 1
#     if i % 1000000000 == 0:
#         print("while")

# control = True 

# yield 

# while True:
#     u = input()
#     if u == "1234":
#         break # bu siklni majburiy toxtatish
#     else:
#         print("wrong") 
#         continue # keyingi siklga o'tish
#         print("try again")
# task 1 
# userdan sonlar qabul qiling (faqat son) va ularni yigindisini hisoblang 
# agar user "stop" ni kiritsa dastur toxtasin va yigindini chop eting  

# count = 0
# while True:
#     num = input("Write..")
#     if num == "stop":
#         break
#     else:
#         num = int(num)
#         count += num 
# print(count)

# task 2
# alpha = "abcdef"
# for letter in enumerate(alpha):
#     print(letter[0]+1 , letter[1])

# task 3
# user 2 xonalikdan katta butun son kiritadi ulardan faqat 0 bilan tugaganlarini summasini hisoblang


