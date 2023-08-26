# task 1 
# 1. Foydalanuvchidan soat nechi ekanini so’rang bu int son bo’ladi , agar qiymat 4 bilan 10 ni orasida bo’lsa print(‘Hayirli tong’)  agar 10 bilan 17 ni orasida bo’lsa print(‘Hayirli kun’) 17 bilan 23 ni orasida print(‘Hayirli kech’) cmd ga chiqadi.

# task 2 
# while orali foydalanuvchidan Ismini va Yoshini kiritishini so’raydigan va ismi nechta belgidan iborat bo’lsa uni yoshiga ko’paytiradgan dastur tuzing.

# task 3 
# Foydalanuvchi bergan sonlar oralig’idagi barcha toq sonlarni listga yozuvchi kod yozing: 
# masalan 5  bilan 10 orasidagi sonlar > nums = [6,7,8,9,10]

# task 4 
# Berilgan qatorda unlilar sonini topadigan dastur yozing topilishi kerak bo’lgan unlilar sifatida (a, i, u,e,o) harflari ko’rib chiqiladi. Kiruvchi matn kichkina harflardan tashkil topgan va probellar bilan ajratilgan bo’lishi mumkin.
import time
import requests # pip install requests
from bs4 import BeautifulSoup as bs  #pip install bs4

url = f"https://ismlar.com/category/Boshqalar"

def connect_to_site(url,index):
    res = requests.get(url+f"?page={index}")
    if res.status_code == 200:
        return res
    else:
        return False

def write_data(data):
    with open("names.txt", "a", encoding='utf-8') as file:
        for line in data:
            file.write(f"{line}, ")
            
def parser(index):
    obj_parse = connect_to_site(url,index)
    print(obj_parse)
    if obj_parse:
        page = bs(obj_parse.text, "html.parser")
        h1 = page.findAll("h1", class_="font-bold text-2xl text-cyan-500")
        names = [x.text.strip() for x in h1]
        print(names)
        write_data(names)
    else:   
        time.sleep(1)
        print("Error")        
    return True

for i in range(1,190):
    done = parser(index=i)
    print(done)
    if done:
        print(i)