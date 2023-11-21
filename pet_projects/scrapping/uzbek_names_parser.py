# pip install beautifulsoup4
import time
import json
import sqlite3
import requests
from bs4 import BeautifulSoup

con = sqlite3.connect("names.db", check_same_thread=False)
cur = con.cursor()

# cur.execute("""CREATE TABLE names( 
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT,
#     description TEXT);""")






for i in range(1,29):
    HEADERS = {
        "User Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    url = f"https://ismlar.com/category/O%E2%80%98zbekcha?gender=1&page={i}"

    page = requests.get(url=url,headers=HEADERS)
    # print(page.status_code) #
    soup = BeautifulSoup(page.content, "html.parser")

    all_names = soup.findAll("li",class_="p-4 rounded-2xl space-y-4 bg-cyan-100")
    data = []
    for name in all_names:
        temp = {
            "name":name.h1.text.strip(),
            "text":name.div.p.text.strip()
        }
        data.append(temp)
   
    with open("./names.json", "+w") as file:
        file.write(json.dumps(data))
    print("page =", i)
    time.sleep(1)
    # for name in all_names:
    #     try:
    #         sql = f"""
    #         INSERT INTO names(name,description)
    #         VALUES('{name.h1.text.strip()}','{name.div.p.text.strip()}');
    #         """
    #         cur.execute(sql)
    #     except sqlite3.DatabaseError as err:
    #         print(err)
    #     else:
    #         con.commit()
    # else:
    #     cur.close()
    #     con.close()
    #     time.sleep(1)
    #     print("OK")
