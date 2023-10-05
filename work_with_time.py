import datetime # sana va vaqt moduli
import time  # vaqt moduli
import calendar # kalendar moduli
import locale
locale.setlocale(locale.LC_ALL, "UZ_uz")
# _now = datetime.datetime.now() 
# print(_now) # 2023-09-26 16:39:01.826321
# print(_now.year)
# print(_now.month)
# print(_now.day)
# print(_now.hour)
# print(_now.minute)
# print(_now.second)
# print(_now.microsecond)

# br_year = 2006
# br_month = 10
# br_day = 10
# print(_now.year - br_year)
# print(_now.month - br_month)
# print(_now.day - br_day)

# _now = datetime.datetime.now() 
# birthday = datetime.date(int(input("Year")),int(input("Month")),int(input("Day"))) 

# days = datetime.date(_now.year,_now.month,_now.day) - birthday
# days = days.days

# year = days // 365
# ots_month = days % 365
# month  = (year * 12) + (ots_month // 12) 
# print(month) 
# print(f"You live :   year={year} , months={month} , and days={days}")
 
# from datetime import time

# print(time.strftime("%Y")) # string format time >> 2023 
# print(time.strftime("%y")) # >> 23 
# print(time.strftime("%m")) # >> oy raqami  
# print(time.strftime("%b")) # >> oy nomi qisqa Sep 
# print(time.strftime("%B")) # >> oy nomi toliq September  
# print(time.strftime("%a")) # >> Tue kun nomi qisqa  
# print(time.strftime("%A")) # >> Tuesday kun nomi toliq  
# print(time.strftime("%M")) # >> minute 
# print(time.strftime("%H")) # >> soat
# print(time.strftime("%S")) # >> sekund
# print(time.strftime("%x")) # >> 09/26/23
# print(time.strftime("%X")) # >> 17:20:55

# text = "Bugun %d - %B , %Y - yil %A.  Soat %H dan %M minut o'tdi."
# print(time.strftime(text)) # Bugun 26 - Sentabr , 2023 - yil seshanba.  Soat 17 dan 24 minut o'tdi.




# for i in range(100):
# 	print(i)
# 	time.sleep(1) # sleep kodni toxtatish , int - sekundlarni qabul qiladi

# timedelta - vaqt oraligini hisoblash imkoni
# dt1 = datetime.timedelta(weeks=2,days=4,hours=12,minutes=30,seconds=12)
# dt2 = datetime.timedelta(weeks=1,days=1,hours=5,minutes=40,seconds=10)
# print(dt1 - dt2) # vaqt oraligi : 10 days, 6:50:02

# # date - sana obyekti 
# print(datetime.date(2023,10,3)) # 2023-10-03

# # calendar - kalendar obyekti
# c = calendar.TextCalendar() # oddiy matn kalendar
# # c = calendar.HTMLCalendar() # html teglari orqali hosil qilingan kalendar
# print(c.formatyear(2023)) # yil kalendari
# print(c.formatmonth(2023,10)) # oy kalendari
