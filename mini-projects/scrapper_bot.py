# Send jokes from jokes.json
import json
import random
from telepot import Bot

bot = Bot(token="")

g_id = None
jokes = None

with open("jokes.json", "r", encoding="utf-8") as file:
    jokes = json.loads(file.read())
random_joke_key = list(jokes.keys())[random.randint(0, len(jokes.keys())-1)]

bot.sendMessage(g_id, jokes.get(random_joke_key))

# Jokes parsing from latifa.uz

# import requests
# import json
# import time
# import random
# from bs4 import BeautifulSoup as bs


# jokes = {}

# i = random.randint(1,500)
# url = f"https://latifa.uz/?page={i}"
# ten_jokes = {}
# HEADER = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
# }
# page = requests.get(url=url, headers=HEADER)
# soup = bs(page.text, "html.parser")
# divs = soup.findAll("div", attrs={'data-id' : True})   

# for i in divs:
#     text = i.text.replace("\n", "").replace("\\", "").replace('\"', '"').replace("\r", "")
#     ten_jokes.update({f"{i['data-id']}":text})
# jokes.update(ten_jokes)
# print("get 10 jokes")
# time.sleep(5)        
    

# with open("jokes.json", "w+", encoding="utf-8") as file:
#     file.write(json.dumps(jokes,ensure_ascii=False))