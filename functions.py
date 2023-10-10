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

# def fub(**args):
#     if len(args)<2:
#         return args
#     else:
#         return args[-2:]
# print(fub(3,45,32,2))

# print(summa(1,2,3,4,5)) # 15

# def kwargs_summa(**kwargs):
#     print(kwargs) # {'a': 1, 'b': 2, 'c': 3, 'd': 14, 'e': 5} - dict values
#     amount = 0
#     for i in kwargs.values():
#          amount += i
#     return amount
# print(kwargs_summa(a=1,b=2,c=3,d=4,e=5)) # 15
# def ten(**kwargs):
#     for k,v in kwargs.items():
#         if v>10:
#             print(k)
# ten(a=1,b=13,c=16)
def super_func(*args, **kwargs):
    return [k for k,v in kwargs.items() if v in args]

# super_func(1,2,number1=3,number2=2)

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



# arr = [1,2,4,5,9,7,8,3,21,5,6,4,89]
# # print(filter(lambda x:x>50, arr)) # <filter object at 0x00000265FA203C70>
# print(list(filter(lambda x:x>20, arr))) # [21, 89]

# zip - berilgan ikita ketma-ketlikdan har bir takrorlanishda bittadan element olib tuple qaytardi

# letter = "abcde"
# nums = [1,2,3,4]
# print(zip(letter,nums)) # <zip object at 0x00000227160CE180>
# print(list(zip(letter,nums))) # [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

# print([x for x in range(10) if x > 5]) # [6, 7, 8, 9]

# lorem = "lorem ipsum dolor amet"
# numbers = [1,2,3,4]

# d = {k:z for k,z in zip(lorem.split(' '),numbers)}
# print(d) # {'lorem': 1, 'ipsum': 2, 'dolor': 3, 'amet': 4}

# map - berilgan ketma-ketlik elementlari uchun berilgan funksiyani qollaydi 
# lorem = "lorem ipsum dolor amet"
# print(list(map(lambda x: x.upper(), lorem.split(" ")))) # ['LOREM', 'IPSUM', 'DOLOR', 'AMET']
text =  """
An asterisk pyramid may not be the most useful example, but it surely tests your understanding of loops and maths in Python.

To create a pyramid, you need to start with 1 asterisk. On the next line you have 3, then 5,7, and so on. In other words, the number of asterisks is 2*i + 1, where i is the row number (or the height) of the pyramid.

Now you got the number of asterisks.

Then you need to know how many spaces you need to the left of the asterisks to make it look like a pyramid.

In the first row, the number of spaces is the same as the height of the pyramid. Then on the second row, it is one less. On the third one less again. So you need to add one less space for each row of asterisks. In other words, the number of spaces is h-i-1, where h is the pyramid height and i is the row number.
"""

# task 1 
# userdan harf qabul qiling va shu harf bilan boshlanadigan barcha sozlarni text o'zgaruvchisi ichidan topib list korinishida ekranga chiqaring
s=input('>>>')
print([item for item in text.lower().split(' ') if item[0]==s.lower()])