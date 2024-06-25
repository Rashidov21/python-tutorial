# for , while 
# for - sanoqli takrorlanish 
# while - to'xtovsiz takrorlanish 

# print(1)
# print(2)
# print(3)
# print(4)

# for <sanoq boshi o'zgaruvchi elon qilinadi> in <ketma ketlik>:
#     bu yerda takrorlanishi kerak bolgan kod 

# for i in "salom":
#     print(i)

# range - sonlar diapazoni 
# nums = range(10) # 0 dan 10 gacha sonlar 
# print(nums) # range(0, 10)
# nums = range(2,15) # 2 dan 15 gacha sonlar 
# print(nums) # range(2, 15)
# nums = range(5,15,2) # 5 dan 15 gacha sonlar 2 tadan orada tashlab 
# print(nums) # range(5, 15, 2)
# for i in range(10):print(i, end="") # 0123456789
# for i in range(2,15):print(i, end="") # 234567891011121314
# for i in range(5,15,2):print(i, end="") # 5791113

# for i in range(1,11):
#     print(i)

# i - iteration > takrorlanish
# for watermelon in "fruits":
#     print(watermelon)

# i , k , j , x - kabi o'zgaruvchilarni elon qilish afzal
# for i,k in [("a","b"),("c","d")]:
#     print(i,k)

# nums = []
# for i in range(1,21):
#     if i % 2 == 0:
#         nums.append(i)
        
# print(nums) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# print([i for i in range(1,21) if i % 2 == 0]) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# for i in range(5):
#     print(i)
# else:
#     print("takrorlanish tugadi")

# while 
# n = 10

# while 0 < n:
#     n -= 1 # -= > ayrib tenglash
#     print(n)
# i = 0
# while i < 10:
#     i += 1
#     if i == 5:
#         break # break - majburan tsiklni to'xtatish
#     print(i)
# i = 0
# while i < 10:
#     print(i)
#     i += 1
# else:
#     print("takrorlanishlar tugaganidan so'ng ishlaydigan kod")

# while True:
#     num = int(input("Son kiriting :"))
#     if num == 7:
#         print("Topdiz")
#         break
#     else:
#         print("Notog'ri")
#         continue # keyin takrorlanishga o'tish
#     print("koooo")
