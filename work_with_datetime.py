import time
import datetime

import locale
locale.setlocale(locale.LC_ALL, "UZ-uz")

now = datetime.datetime.now() # joriy sana va vaqt ni qaytaradi
# print(type(now)) # <class 'datetime.datetime'>
# print(dir(now))

# print(now.year)
# print(now.month)
# print(now.day)

# string_format_time = time.strftime("%d-%m-%Y %H:%M:%S")
# print(string_format_time) # 11-07-2024 21:12:24 >> string format time\
# print(time.strftime("%d"))
# print(time.strftime("%m"))
# print(time.strftime("%Y"))
# print(time.strftime("%A")) # hafta kuni nomi to'liq
# print(time.strftime("%a")) # hafta kuni nomi qisqa
# print(time.strftime("%B")) # oy nomi toliq
# print(time.strftime("%b")) # oy nomi qisqa

# print(time.strftime("%x")) # 11/07/2024
# print(time.strftime("%X")) # 21:18:07


# for i in range(10):
#     time.sleep(1) # 1 sekundga dasturni uxlatish
#     print(i)

# first_date = datetime.timedelta(weeks=2,days=5,hours=10)
# second_date = datetime.timedelta(weeks=1,days=4,hours=2)
# print(first_date - second_date) # 8 days, 8:00:00

# d1 = datetime.date(2024,7,11)
# d2 = datetime.date(2024,8,25)
# print(d2 - d1) # 45 days, 0:00:00

# print(datetime.date.today()) # joriy sana > 2024-07-11
# print(datetime.date.today().year)
# print(datetime.date.today().month)
# print(datetime.date.today().day)

# task 1 
# userdan tugilgan sanasini qabul qiling va joriy sanaga qadar necha kun yashaganini ekanini hisoblang
# input: 1995-10-30
# output: 10,482 kun
# b = "1995-10-30"
# print(b.split("-")) # ['1995', '10', '30']

# "YYYY-MM-DD"

# task 2
# userdan 3 son qabul qiling 1-son va 2 son orasidagi tasodify sonlardan iborat 3 son miqdorida massiv hosil qiling 
# input: 5,60,500
# output : [5, 6, 24, 28, 55]