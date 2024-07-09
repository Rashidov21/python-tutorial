# set - unikal tartibsiz elementlar to'plami 
# frozenset - unikal o'zgarmas tartibsiz elementlar to'plami

# s = set("python python")
# # s = {}
# print(s)

# s1 = set("abc")
# s2 = set("def")

# print(s2.union(s1)) # {'f', 'd', 'c', 'e', 'a', 'b'}

# s = set()
# s.add(1) # yangi narsa qo'shish uchun 
# s.update([4, 5, 6]) # setni yangilash 
# s.remove(6) # biror bir elementni ochirish
# # s.remove(10) # Key error 
# s.discard(10) # korsatilgan elementni ochiradi agar element bolmasa xatolik bermaydi
# s.pop() # tasodify elementni ochiradi
# # s.clear() # setni tozalash
# print(s) # {1, 4, 5}

# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# result = set1.difference(set2)
# print(result)  # {1}

# fset = frozenset("python")
# print(dir(fset))



# DICT 
# d = dict(a=1,b=2,c=3)
# print(d) # {'a': 1, 'b': 2, 'c': 3}
# person = {"name":"John","age":20,"salary":1500}
# print(person) # {'name': 'John', 'age': 20, 'salary': 1500}

# person = {"name":"John","age":20,"salary":1500}

# print(person.get("name")) # John
# print(person["name"])# John
# # print(person["skills"])# KeyError: 'skills'
# print(person.get("skills")) # None

# d = {}
# d["key1"] = 1
# d["key2"] = 2
# print(d) # {'key1': 1, 'key2': 2}
# d["key1"] = 0
# print(d)  # {'key1': 0, 'key2': 2}

# setdefault  - mavjud kalit orqali elementni olish yoki uni hosil qilish 

# d = {"key1":1}
# print(d.setdefault("key1")) # 1
# print(d.setdefault("key2",2)) # 2
# print(d) # {'key1': 1, 'key2': 2}

# del d["key1"] 
# print(d) # {'key2': 2}

# d = dict(a=1,b=2,c=3)

# print(d.keys()) # dict_keys
# print(d.values()) # dict_values
# print(d.items()) # dict_items

# for i in d.keys():
#     print(i)
# for i in d.values():
#     print(i)
# for i in d.items():
#     print(i)

# d = dict(a=1,b=2,c=3)

# d.pop("a")
# r = d.popitem() # tasodify bir elementni ochirish
# print(r) # ('c', 3)
# d.update({"d":4}) # boshqa dict bilan yangilash
# d.clear() # {}
# d_copy = d.copy() # nusxalash
# print(d_copy) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print(d) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}



s = "abc"
n = [1,2,3]
d = {}
for i in range(len(s)):
    d.update({s[i]:n[i]})
print(d) # {'a': 1, 'b': 2, 'c': 3}

print({k:v for k,v in zip("abc",[1,2,3])}) # {'a': 1, 'b': 2, 'c': 3}

print(dict(zip("abc",[1,2,3]))) # {'a': 1, 'b': 2, 'c': 3}