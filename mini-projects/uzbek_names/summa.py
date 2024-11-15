import time
import requests
from bs4 import BeautifulSoup
import sqlite3

# sql = """CREATE TABLE usd(
#     id AUTO_INCREMENT PRIMARY KEY , 
#     name TEXT , 
#     cost DETCIMAL(5,2)
#     );"""

def db_write(id,name,cost):
    con = sqlite3.connect("usd.db", check_same_thread=False)
    cur = con.cursor()
    sql = f"INSERT INTO usd VALUES({id},'{name}',{cost});"
    try:
        cur.execute(sql)
    except sqlite3.DatabaseError as e:
        print(e)
    else:
        con.commit()
        print("Success !")

url = f"https://nbu.uz"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
usd_block = soup.find("div", class_="currency")
usds = usd_block.find("ul").findAll("li")
id = 10
for li in usds[:-1]:
    name = li.text.strip().split("\n")
    if len(name) > 2:
        n = name[0]
        c = name[-1].strip()
        db_write(id,n,c)
        time.sleep(1)
    id += 1
    
    
# task 
# quyidagi jadval korinishida malumotlarni fake moduli orqali hosil qiling va alohida 
# db ga yozing 

# db ni olib undagi kimyo fanidan eng yuqori bal toplagan 3 ta talabani
# db ni olib undagi fizika fanidan eng yuqori bal toplagan 3 ta talabani
# db ni olib undagi biologiya fanidan eng yuqori bal toplagan 3 ta talabani 

# larni alohida qilib chiqaring 

