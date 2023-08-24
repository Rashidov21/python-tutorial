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

