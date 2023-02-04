"""
Download all images from  emoji.wannathis.one home page
"""

import requests
import wget
from bs4 import BeautifulSoup as bs

url = "https://emoji.wannathis.one/"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

page = requests.get(url=url)
print(page.status_code) # if 200 its ok

if page.status_code == 200:
    parsering = bs(page.text, "html.parser")
    images = parsering.findAll("img")
    for i in images:
        # print(i["src"])
        if "Preview" in i["src"]:
            wget.download(i["src"])
        else:
            print("Not emoji image")
else:
    print("Response not found.", "HTTP status code = ", page.status_code)