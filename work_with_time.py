import locale
locale.setlocale(category=locale.LC_ALL, locale="Uz_uz")
import time 
import datetime
import calendar

# Time 
# print(time.time()) # 1970-1-01 > now() ? qancha sekund

# print(time.strftime("%d/%m/%y")) #30/01/23
# print(time.strftime("%d")) #30
# print(time.strftime("%m")) #01 oy
# print(time.strftime("%b")) #jan
# print(time.strftime("%B")) #January
# print(time.strftime("%a")) #Mon
# print(time.strftime("%A")) #Monday
# print(time.strftime("%y")) #23
# print(time.strftime("%Y")) # 2023
# print(time.strftime("%W")) # 05 - yil ichida hafta tartib raqami
# print(time.strftime("%w")) # 1 - hafta ichidan kunni tartib raqami
# print(time.strftime("%H")) # soat
# print(time.strftime("%M")) # minut
# print(time.strftime("%S")) # sekund
# print(time.strftime("%I")) # 12 soatlik format
# print(time.strftime("%x")) # 30/01/2023 - joriy vaqt boyicha sana 
# print(time.strftime("%X")) # 16:43:53- joriy vaqt boyicha vaqt 

# print(time.strftime("%Y/%m/%d %H:%M:%S")) #2023/01/30 16:47:03
# print(time.strftime("%x %X")) #30/01/2023 16:47:30

# time.sleep(3)
# print("3 sekund tugadi")
# for i in range(10):
#     time.sleep(1)
#     print(i)



# Date and time 
# now = datetime.datetime.now()
# print(now) # 2023-01-30 16:20:17.231639
# print(type(now)) #<class 'datetime.datetime'>
# print(dir(now))

# day = now.day
# month = now.month
# year = now.year
# print(day) #30
# print(month) #1
# print(year) #2023

# print(year + 2) #2025

# task 1 
# user yoshini yil va kunlarda aniqlovchi dastur tuzing

# now = datetime.datetime.today()
# a = datetime.timedelta(days=10, hours=5)
# b = datetime.timedelta(days=5, hours=2, minutes=30)

# print(a - b)  #5 days, 2:30:00
# tomorrow = datetime.datetime(2023,1,31)
# today = datetime.date.today() #<yil oy kun>
# print(today) #2023-01-30
# print(today == tomorrow) #False
# print(today == today) #True

# start_date = datetime.date.today()
# # print(end_date)
# end_date = start_date + datetime.timedelta(days=7)
# print(end_date) #2023-02-06
# print(today == end_date) #False

# start_time = datetime.time(hour=1, minute=30, second=30)
# end_time = datetime.time(hour=0, minute=30, second=30)
# print(start_time-end_time)

# print(datetime.time.min)
# print(datetime.time.max)
# print(datetime.time.resolution)

# c = calendar.LocaleHTMLCalendar()
# print(c.formatyear(datetime.date.today().year))
# c = calendar.LocaleTextCalendar()
# print(c.formatyear(datetime.date.today().year))


# from timeit import Timer

# code = """\
# i = 1
# while i < 10**5:
#     i = i + 1

# """
# t = Timer(stmt=code)
# print("While : \n",t.timeit(number=1000))