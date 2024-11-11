# pip install beautifulsoup4
# pip install requests
import time
import requests
from bs4 import BeautifulSoup
from db import db_write,get_last_item_id
id = 1



for i in range(1,337):
    
    url = f"https://ismlar.com/category/Arabcha?page={i}"
    page = requests.get(url)
    # print(page.status_code)
    soup = BeautifulSoup(page.text, "html.parser")
    names_block = soup.find("ul", class_="list-none space-y-2")
    name_block = names_block.findAll("li")
    for name in name_block:
        n = name.h1.text.strip()
        d = name.p.text.strip()
        db_write(id,n,d)
        id += 1
    time.sleep(2)
    print(url)