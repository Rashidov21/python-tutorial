# d = dict(name="John Doe", age=30)
# print(d) #{'name': 'John Doe', 'age': 30}

# d = {
#     "name":"John",
#     "surname":"Doe",
#     "age":20
# }
# print(d) #{'name': 'John', 'surname': 'Doe', 'age': 20}

# print(d["name"]) # John
# print(d["money"]) # KeyError: 'money'
# print(d.get("name")) # John - get_object_or_404 >> get or None
# print(d.get("money")) #  None
# k = ["monkey", "elephant"]
# v = [12,5]

# print(dict(zip(k,v))) # {'monkey': 12, 'elephant': 5}
# import random
# from faker import Faker

# fake = Faker()

# users = {}

# for i in range(10):
#     name = fake.name()
#     temp = {
#         f'{name.split(" ")[0].lower()}': random.randint(18,30)
#     }
#     users.update(temp)
# print(users)
# d = {}

# d["name"] = "John Doe"

# print(d) # {'name': 'John Doe'}

# print(d.get("name")) # John Doe

# print(d.setdefault("name", "No name")) # John Doe
# print(d.setdefault("age", 20)) # 20

# print(len(d)) # 2
# del d["name"] # element ochirish

# print(d) # {'age': 20}

d = {}

d["name"] = "John Doe"
d["age"] = 20

# for item in d.keys(): # faqat kalitlarini olish
#     print(item)

# for item in d.items(): # elementlarini olish
#     print(item)

# for item in d.values(): # faqat qiymatlarini olish
#     print(item)
# d.pop("age")  
# print(d) # {'name': 'John Doe'}

# print(d.popitem()) #('age', 20)

# d.clear()
# d.update({"salary":300}) #{'name': 'John Doe', 'age': 20, 'salary': 300}
# print(d)

# keys = "abc"
# values = [1,2,3]

# d = {k: v for (k, v) in zip(keys, values)}
# print(d) #{'a': 1, 'b': 2, 'c': 3}

