# import locale
# locale.setlocale(locale.LC_ALL, "UZ-uz")
# import datetime
# from time import strftime
# n = datetime.datetime.now()
# print(n.strftime("%B")) # Iyul
# s1 = ''
# s2 = ""
# s3 = """"""

# print('Hello'world'')
# print('Hello "world" ')

# s = "salom"
# print(s[0]) # s
# print(s[-1]) # m

# print(len(s)) # 5

# s = str(1)
# print(type(s)) # <class 'str'>

# print("\t\tsalom") # qatorni onga surish
# print("sal\nom") # qatorni yangi qatorga olib otish
# print("salom\a") # windows tovushi

# print("sal\"om") # sal"om
# print("don\'t") # don't
# print("don\\t") # don\t
# print("\uaF60")\
    
    
# s = "Python"
# print(s[10]) # IndexError: string index out of range

# new_s = s[start:stop]
# new_s = s[0:3] # index boyicha elementlarni qirqish
# print(new_s) # Pyt
# s = "Python"
# name = "john"
# age = 23
# # res = "My name is %s , %s years old" % (name,age)
# # print(res) # My name is john , 23 years old

# print("My name is {0} , {1} years old".format(name,age)) # My name is john , 23 years old

# print(f"My name is {name} , {age} years old")# My name is john , 23 years old

# STRING METHODS 

# s = "  Python  "
# print(s)
# print(s.strip()) # qator boshi va oxiridagi probellarni yoki siz korsatgan belgini ochiradi
# print("**salom**".strip("*")) # salom
# lstrip - faqat boshidagi belgilarni ochirish 
# rstrip - faqat oxiridagi belgilarni ochirish 

# s = "python is better language"
# print(s.split(" ")) # qatorni siz korsatgan belgi boyicha bo'lib massivga aylantiradi
# ['python', 'is', 'better', 'language']
# rsplit - ongdan chapga qarab ishlaydi 
# new_str = """разделяет строку на подстроки по символу перевода строки (\п) 
# и добавляет их в список. Символы новой строки включаются в результат, только если 
# необязательный параметр имеет значение True. Если разделитель не найден в строке, то 
# список будет содержать только один элемент. Примеры"""
# print(new_str.splitlines()) # matnni qatorlar boyicha bo'lish
# print(len(new_str.splitlines())) # 4

# print("".join(["salom","qale","ishlar"])) # salomqaleishlar
# join - berilgan ketma ketlik str elementlarini bitta str ga aylantiradi 


# print("salom".upper()) # SALOM
# print("salom".lower()) # salom
# print("salom qale ishlar".title()) # Salom Qale Ishlar
# print("salom qale ishlar".capitalize()) # Salom qale ishlar
# print("SaLoM".swapcase()) # sAlOm

# new_str = "Javascript and Python"

# print(new_str.find("and")) # 11
# print(new_str.find("true")) # -1
# rfind - o'ngdan chapga qarab 
# print(new_str.index("and")) # 11
# print(new_str.index("true")) # ValueError: substring not found
# rindex - o'ngdan chapga qarab 

# new_str = "Javascript and Python"
# print(new_str.count("s")) # 1
# print(new_str.count("t")) # 2
# print(new_str.count("and")) # 1

# print(new_str.startswith("J")) # True
# print(new_str.startswith("Python")) # False

# print(new_str.endswith("J")) # False
# print(new_str.endswith("Python")) # True

# new_str = "Javascript and Python"
# print(new_str.replace("Javascript", "Ruby")) # Ruby and Python


# print("012abc".isalnum()) # True
# print("012?%^ab".isalnum()) # False

# print("abc".isalpha()) # True
# print("abc123".isalpha()) # False

# print("123".isdigit()) # True
# print("123abc".isdigit()) #  False

# print("salom".islower()) # True
# print("Salom".islower()) # False
# print("salom".isupper()) # False
# print("SALOM".isupper()) # True
# print(" ".isspace()) # True
# print("**".isspace()) # False