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
import random
from faker import Faker

fake = Faker()

users = {}

for i in range(10):
    name = fake.name()
    temp = {
        f'{name.split(" ")[0].lower()}': random.randint(18,30)
    }
    users.update(temp)
print(users)