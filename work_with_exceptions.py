# try 
# except
# else
# finally
# raise

# with open("test.txt", "r") as f:
#         print("Faylni o'qish...")
#         print(f.read())

# try: # xatolik bolishi mumkin bolgan kod
#     with open("test.txt", "r") as f:
#         print("Faylni o'qish...")
#         print(f.read())
# except FileNotFoundError: # xatolik vujudga kelsa ishlashi kerak bolgan kod
#     print("Fayl topilmadi!")
# else: # xatolik bolmasa ishlaydigan kod
#     print("Fayl muvaffaqiyatli o'qildi!")
# finally: # har qanday holatda ham ishlaydigan kod
#     print("Kod bajarildi!")
    
# try:
#     x = 1 / 0
# except Exception as error:
#     print("Xatolik! = ", error)

# task 1
# NameError uchun try except yordamida xatolikni tutamiz va konsolga chiqaramiz 
# try:
#     print(x)
# except NameError:
#     print("Xatolik!")

# task 2 
# Fayldan ma’lumot o’qish va teskari chiqarish
# Vazifa: input.txt nomli matnli fayldan ma'lumotlarni o'qing va har bir qatordagi so'zlarni teskari tartibda ekranga chiqaring. Agar fayl bo'lmasa, “Fayl topilmadi” deb xabar bering.
# input: olma anor behi 
# output: behi anor olma  

# try:
#     with open("input.txt", "r") as f:
#         l = f.read().split(" ")
#         l.reverse()
#         print(" ".join(l))
# except FileNotFoundError:
#     print("Fayl topilmadi!")
    
# print(" ".join(list(reversed(open("input.txt").read().split(" ")))))

