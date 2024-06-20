# Data Type - Ma'lumot turi
# Data Structure - Ma'lumot tuzilmasi
# x = 10
# x = {"key":30}

# Dastur :
# 1 - malumotlarni qabul qilish
# 2 - ularni qayta ishlash 
# 3 - saqlash 
# 4 - natijani qaytaradi 


# b = True 
# print(type(b)) # ma'lumotni qaysi turga tegishli ekanini bilish  | <class 'bool'>

# bool - True, False - Ha , Yoq
# None - Qiymat mavjud emasligini bildiradi 
# int - butun sonlar 
# float - qoldiqli sonlar 
# str - string , satr, qator , matn 
# list - ro'yhatlar, array, massiv - tartibli elementlar ketma-ketligi
# tuple - kortej - tartibli o'zgarmas elementlar ketma-ketligi
# dict - lug'at, elementlariga kalit yordamida murojaat qilinadigan obyektlar toplami
# range - sonlar diapazoni (oraligi)
# set - unikal tartibsiz elementlar to'plami 
# frozenset - unikal o'zgarmas tartibsiz elementlar to'plami 


# x,y,z = 1,2,3
# print(x + y + z) # 6

# a,b,*c = [1,2,3,4,5]
# print(a,b,c) # 1 2 [3, 4, 5]

# print("10" + "10") # 1010 
# print(int("10") + int("10")) # 20
# print(str(10) + str(10)) #  1010

# print(int("12.5")) # ValueError: invalid literal for int() with base 10: '12.5'
# print(int("python")) # ValueError: invalid literal for int() with base 10: 'python'

# print(str(10) + 2)
# print(str(-12) - 2)
# print(str(1.3) + 12)
# print("python" * 5) # pythonpythonpythonpythonpython

# Har qanday son boolean da bu True faqat 0 dan tashqari 

# print(bool(10)) # True
# print(bool(0)) # False
# print(bool(-10)) # True

# Bosh qator bu False bo'sh bo'lmagan har qanday qator bu TRue 
# print(bool("")) # False
# print(bool(" ")) # True

# user_i = int(input())
# user_f = float(input())
# x = 5
# del x # o'zgaruvchini o'chirib yuborish
# print(x) # NameError: name 'x' is not defined

# Arifmetika 
# print(2 + 2) # 4
# print(4 - 2) # 2
# print(2 * 2) # 4
# print(4 / 2) # 2.0
# print(4 // 2) # 2
# print(4 ** 2) # 16
# print(7 % 3) # 1
# print(8 % 2) # 0

# print((10 - 2) * (8 // 4)) # 16

# in , not in , is 

# in - mavjudlikka tekshirish > bool 
# print("s" in "salom") # True
# print("t" in "salom") # False

# not in - mavjud emas ekanini takshirish > bool
# print("t" not in "salom") # True

# is - ozgaruvchilar xotirani bitta katakchasiga yol korsatganda True aks holda False ni qaytaradi
# x = 10
# y = x 
# z = 5

# print(x is y) # True
# print(x is z) # False
# print(x is not z) # True

# Taqqoslash operatorlari > bool 

# x = 2 
# y = 3
# print(x == y) # False 
# print(x != y) # True 

# print(x < y) # True - katta ekanligiga tekshirish
# print(x < y) # True
# print(x <= y) # True - katta yoki teng ekanligiga tekshirish 
# print(x >= y) # False

# Mantiqiy operatorlari > bool 
# and - mantiqiy VA 
# or - mantiqiy YOKI
# not - mantiqiy EMAS

# print(1 and 0) # 0
# print(1 and 1) # 1

# a = 2
# b = 3
# c = 6
# d = 4
# print(a < b and c > d) # True

# print(1 or 0) # 1

# print(not True) # False
# print(not False) # True

# print(1 and 0 or 2 > 3 and 1 < 8) # False

# x = 0
# if not x:
#     print("OK")
   
#    asdgs 