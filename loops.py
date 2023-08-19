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

k = 5
n = int(input("N ?"))
if n > 0:
    for i in range(n):
        print(k)