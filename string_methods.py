# s = ''
# s = ""
# s = """"""
# s = 'Salom "yaxshimisan" ?' 

# s = 'don\"t'
# print(s) # don't , don"t

# long_str = "Lorem Ipsum has been the industry's standard dummy text ever since the \
# unknown printer took a galley of type and scrambled it to make a type specimen book"
# print(long_str)

# print("\tlorem\nipsum") #
# r-string 
# print(r"\tlorem\n ipsum") #\tlorem\n ipsum
# f-string 
# apple = 10500
# print(f" 4kg Olma = {4*apple}") #  4kg Olma = 42000
# watermelon = 3*2000

# print("3k tarvuz = %s" %watermelon) #3k tarvuz = 6000
# print("2kg tarvuz = {0}\n4kg Olma = {1}".format(2*2000,4*apple))
# 2kg tarvuz = 4000
# 4kg Olma = 42000


# string methods 
# short_str = "lorem ipsum dolor"
# print(short_str[0], short_str[1]) # l o
# print(short_str[len(short_str)-1]) # r

# print(short_str[-1]) # r
# 0 , 1
# -1 , -2
# short_str = "lorem"
# start = 2
# stop = 5
# print(short_str[start:stop]) # rem
# print(short_str[:stop]) # lorem
# print(short_str[start:]) # rem

# print("Hello world"[6:]) # world
# print("Hello world"[:6]) # Hello

# text = "lorem ipsum dolor amet sit"
# print(text[len(text)//2:]) # olor amet sit
# print("dolor"[::-1]) # rolod

# for i in range(len("python")):
#     print(i)

# text = "lorem ipsum dolor"
# print(text.center(15,'*'))

# print(type(str(12345))) # <class 'str'>
# print(repr("\no\t")) # '\no\t'

# strip - boshi va oxiridagi siz korsatgan elementlarni ochiradi
# text = "lorem\n"
# print(text.strip("\n")) # lorem
# print(repr(text)) # 'lorem\n'
# print(repr(text.strip("\n"))) # 'lorem'
# print("\tdolor\t".rstrip("\t"))
# print("\tdolor\t".lstrip("\t"))

# text = "lorem ipsum\ndolor amet sit"
# print(text.split(" ")) # ['lorem', 'ipsum', 'dolor', 'amet', 'sit']
# print(text.split(" ",2)) # ['lorem', 'ipsum', 'dolor amet sit']
# print(text.splitlines()) # ['lorem ipsum', 'dolor amet sit']

# text = "Google's service, offered free of charge, instantly translates words, phrases, and web pages between English, over 100 other,languages."
# print("".join(text.split(","))) # str

# text = "lorem ipsum dolor".split(" ")
# print(text)  # ['lorem', 'ipsum', 'dolor']
# print("".join(text)) # loremipsumdolor

# import locale
# import calendar

# locale.setlocale(locale.LC_ALL, "UZ_uz") # lokal tilni uzbek tiliga otqazish
# # locale.setlocale(locale.LC_ALL, "Russian_Russia.1251") # ruscha
# cal = calendar.HTMLCalendar() # html kalendar obyekti
# # print(cal.formatyear(2023)) # html teglardan iborat kalendar
# cal = calendar.TextCalendar() # oddiy matnli kalenda
# print(cal.formatyear(2023)) # yil
# print(cal.formatmonth(2023,9)) # yildagi oy

# print("lorem".upper())
# print("LOREM".lower())
# print("lorem".title())
# print("lorem".casefold())
# print("lorem".capitalize())

# s = "Abdullo olmani yeb qoydi."
# print(s.find("olma")) # 8 : siz qidirgan matnni boshlanish indeksini qaytaradi
# print(s.find("temir")) # agar topa olmasa >> -1

# print(s.index("olma")) # 8
# print(s.index("temir")) # ValueError : substring not found

# task 1 
# string = "John olmani yeb qoydi , yeb qoydi." >> Jhn lmani yeb qydi , yeb qydi.

# string = "John olmani yeb qoydi , yeb qoydi."
# print("".join(string.split("o")))
# print("".join(list(filter(lambda x: x != "o", [i for i in string]))))

# print("assalomu alaykum".count("a")) #4
# print("assalomu alaykum".startswith("as")) # True
# print("assalomu alaykum".endswith("kum")) # True
# print("assalomu alaykum".endswith("tara")) # False
# print("assalomu alaykum".replace("a","o")) # ossolomu oloykum
# print("John olmani yeb qoydi , yeb qoydi.".replace("o",""))
# print("1A".isalnum()) # True
# print("1A#".isalnum()) # False

# print("aA".isalpha())
# print("a1".isalpha())

# print("12".isdigit()) # TRue
# print("1.2".isdigit()) # False

# task 2 
# userdan tel nomer sorang va uni + belgisiz aniq 12 ta raqam ekanini tekshiring
# u = "+998912021030"
# if u.startswith("+"):
#     u = u.replace("+", "")
#     if u.startswith("998"):
#         if u.isdigit() and len(u) == 12:
#             print(u)

# print("12".isdecimal()) # True


# print("ONO".isupper()) # True
# print("ONO".islower()) # False
# print("ONO".istitle()) # False
# print("  ".isspace()) # True
# print("ыовао".isspace()) # False


# import hashlib
# s = "python" # 48 bit 
# h = hashlib.sha1(b"password")
# print(h.digest()) # b'[\xaaa\xe4\xc9\xb9??\x06\x82%\x0bl\xf83\x1b~\xe6\x8f\xd8'
# print(h.hexdigest()) # 5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8


print(len([data for line in open("readFile.py") for data in line.strip().split(" ") if data == ' ']))