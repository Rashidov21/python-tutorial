# try:
#     x = 1 / 0 # xatolik bo'lishi mumkin bo'lgan kod
# except Exception as err:
#     print(err) # xatolik topilsa ishlaydigan kod 
# else:
#     print("Xatolik yo'q") # xatolik bo'lmasa ishlaydigan kod
# finally:
#     print("Baribir ishga tushadigan kod !")

# try:
#     num = int(input("Integer : "))
# except:
#     print("Not integer value !")
# else:
#     print(num)

# 1-Syntax
# 2-Logical 
# 3-On working  

# BaseException - barcha xatoliklarni otasi 
# Exception - dastur xatoliklari 

# email = input("Email :")

# if "@" not in email:
#     raise ValueError("Email noto'g'ri ! @ belgisi yo'q !")
# else:
#     print("To'g'ri !")

# task 1 
# data = "1st 2 3-chi 5 ta 4ta 8dona 9 marta"
# quyidagi matnni probellar orqali ajratib , ajratilgan sonlarni butun songa aylantirib massivga yozing
# agar ajratilgan sonni butun songa aylantirish iloji bo'lmasa try except dan foydalanib xatolikni chetlab o'ting va keyingi songa o'tib dasturni davom ettiring