import datetime

# def get_user_full_name():
#     return "John" +" " + "Doe"
# get_user_full_name() # John Doe
# print(get_user_full_name()) # John Doe


# def funkisya nomi(qabul qiluvchi parametrlari):
#     funksiyani tana kodlari 
    
#     return funksiya qaytaruvchi natija 

# user_date = input("YYYY/MM/DD")

# def get_user_age(user_birthday):
#     today = datetime.datetime.now()
#     user_age = today.year - int(user_birthday.split("/")[0])
#     return user_age
# print(get_user_age(user_date))

# task 1 
# user telefon raqamini kiritsa uni ohirgi 4 ta raqamini 2 xonali qilib bir biriga qoshib qaytaruvchi funksiya yozing 
# input : 93-123-45-67
# output : 112

# def show_phone_number_result(phone_number):
#     pass

# num = input("xx-xxx-xx-xx")
# print(show_phone_number_result(num))

# def main(a=0,b=0):
#     print(a+b)
#     return a + b
# main("Salom", "Alik") # SalomAlik
# main(1,2) # 3

# # main() # TypeError: main() missing 2 required positional arguments: 'a' and 'b'
# # main(2) # TypeError: main() missing 2 required positional arguments: 'a' and 'b'
# # main(1,1) # 2
# main() # 0

# task 2 
# funksiya yozing u foydalanuvchidan list qabul qiladi listda 0 dan 30 gacha tasodifiy 5 ta son bo'ladi va shu list ichidagi sonlar yigindisini qaytaradi 



# def summa(x,y):
#     return x + y 

# print(summa(1,1)) # 2
# print(summa(x=2,y=2)) # 4


# *args, **kwargs

# a,c,*d = 1,2,3,4,5,6
# print(d) # [3, 4, 5, 6]
# def summa(*args):
#     print(args) # (1, 2, 3, 4, 5) - tuple object 
#     amount = 0
#     for i in args:
#         amount += i
#     return amount

# print(summa(1,2,3,4,5)) # 15

# def kwargs_summa(**kwargs):
#     print(kwargs) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5} - dict values
#     amount = 0
#     for i in kwargs.values():
#          amount += i
#     return amount
# print(kwargs_summa(a=1,b=2,c=3,d=4,e=5)) # 15

# def super_func(*args, **kwargs):
#     print(args) # (1, 2)
#     print(kwargs) # {'number1': 3, 'number2': 4}

# super_func(1,2,number1=3,number2=4)

# # anonim function
# summa = lambda x: x + 1

# print(summa(1)) # 2

# def main(x):
#     if x > 10:
#         s = lambda num : num ** 2
#         return s(x)
#     else:
#         return x + 2
# print(main(x=2)) # 
# print(main(x=15)) #

# zip(),filter(), map() 

# arr = list(range(1,30,3)) # 
# print(arr) # [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]

# # version 1 
# temp = []
# for i in arr:
#     if i % 2 == 1:
#         temp.append(i)
# print(temp) # [1, 7, 13, 19, 25]

# # version 2 
# print([x for x in arr if x % 2 == 1]) # [1, 7, 13, 19, 25]

# # version 3 
# print(list(filter(lambda x: x % 2 == 1, arr))) # [1, 7, 13, 19, 25]
# # filter - alohida funksiyani qabul qiladi va ketma-ketlikdagi barcha elementni shu funksiyaqa qarab filterlaydi
# # misol : 
# print(list(filter(lambda num:num>2,[1,2,3,4]))) # [3, 4]


# task 1 
# filter yordamida va lambda funksiyani ishlatgan holatda ushbu dict dan faqat 20 dan katta qiymatga ega bo'lgan dict elementlarini alohida massivga yozuvchi funksiya yozing
# input: {'a':'55','b':'5','c':'12','d':'23','e':'45','e':'11','f':'36','h':'2'}
# output: [{'a':'55'}, {'d':'23'}, {'e':'45'},{'f':'36'}]

# task 2
"""1 noyabrdan boshlab, xonadonlarning oylik energiya iste’moli 1000 kWhdan oshgan taqdirda, bu miqdordan ortiq hajmdagi energiya uchun 2 barobardan 4 barobargacha oshirilgan tariflarda hisob-kitob qilinadi. Bu tartib respublikadagi 7,6 millionta xonadonning qariyb 150 mingtasiga – aksar holatlarda o‘ziga to‘q yoki badavlat aholi qatlamiga ta’sir qiladi, shu orqali mazkur toifaning davlat budjetidan arzon energiya uchun istagancha miqdorda subsidiya olish imkoniyati yo‘qoladi."""

# ushbu matndagi barcha sonlarni yigindisini hisoblang

# task 3 
# xx−xxx−xx−xx korinishida userdan telefon raqam qabul qiluvchi dastur tuzing agar user xato kiritgan bolsa ularni to'g'irlab huddi shu holatda ekranga chiqaring
# input: 998999005
# output:99-899-90-05