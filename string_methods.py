
# import locale
# import calendar
# locale.setlocale(locale.LC_ALL, "uz_UZ")

# cal = calendar.LocaleHTMLCalendar()
# print(cal.formatyear(2023))

# s = "Python"

# print(s[0], s[1]) # P y
# print(s[6]) # IndexError: string index out of range

# num_str = str(123)
# print(num_str + 4) #  TypeError: can only concatenate str (not "int") to str
# print(num_str + "4") # 1234

# print("symblo \n new line ")
# print("symblo \t tab")
# print("assolumu \n alaykum")
# print(r"assolumu \n alaykum") #assolumu \n alaykum
# print("\U0001f604")
# print("\U0001F471")
# print("")
# s = """en.wikipedia.org›List of Unicode characters \
# As of Unicode version 15.0, there are 149,186 characters with code points, covering 161 modernhistorical scripts, as well as \\ multiple symbol sets. / This article includes the 1062 characters in the Multilingual European Character Set 2 (MES-2) sub... Читать ещё"""
# print(s)
# s = "bu 'qora' olma"
# s = 'bu "qora" olma'

# print(s[-1])
# print(s[len(s)-1])

# s = "ruby on rails"
# # on = s[0:5]
# # print(len(on)) #5
# # print(on) #ruby
# print(s[:3])
# print(s[3:])
# print(s[:]) # string copy
# print("kitob"[::-1]) # botik

# age = 30
# name = "John Doe"

# # Python V2
# user = "name = %s, age = %s"  % (name, age) # name = John Doe, age = 30
# print(user)

# user = "name = {0}, age = {1}".format(name, age) # name = John Doe, age = 30
# print(user)

# # Python V3 
# user = f"name = {name}, age = {age}" # name = John Doe, age = 30
# print(user)

# s = "Python string methods"
# print(s.center(50))

# print(ascii("p"))
# s = " salom,xayr,qale " # boshi va oxiridagi probellarni ochirish
# print(len(s))
# print(len(s.strip()))
# print(len(s.lstrip()))
# print(len(s.rstrip()))

# print(s.split(",")) #[' salom', 'xayr', 'qale ']

# s = """en.wikipedia.org›List of Unicode characters \
# As of Unicode version 15.0, there are 149,186 characters with code \n points, covering 161 modernhistorical scripts, as well as \\ multiple symbol \nsets. / This article includes the 1062 characters in the Multilingual European Character Set 2 (MES-2) sub... Читать ещё"""
# print(len(s.splitlines()))
# print(s.splitlines())

# h = "hohla ishla hohla ishlama"
# without_h = h.split("h")
# print(without_h)
# print("".join(without_h)) # ola isla ola islama
# print("".join([1,2,3])) # 123

# print("Python".upper())
# print("Python".lower())
# print("Python".swapcase())
# print("Python".capitalize())
# print("Python is better".title())
# print("Python is better".find("is")) #7
# print("Python is better".rfind("b")) #10
# print("Python is better".index("is")) #7
# print("on table non table".count("on")) #2
# print("aloha chicas".replace("chicas", "muchachos"))
# # print("Python is better".index("qq")) #ValueError: substring not found
# print("gandi".startswith("gan")) # True
# print("gandi".endswith("gan")) # False

# task 1 
# Foydalanuvchidan matn qabul qiling , unda "gaz" , "svet", "yo'q" kabi so'zlar ishtirok etganmi yoki yo'qmi aniqlang va ular sonini har birini alohida hisoblang boring so'zlar register turi yoki boshqa qoshimchalar bilan kelishi mumkin bularni ham inobatga oling