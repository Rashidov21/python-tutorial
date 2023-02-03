import requests
import wget
from bs4 import BeautifulSoup as bs

url = "your url"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

page = requests.get(url=url, headers=headers)
print(page.status_code) # if 200 its ok

if page.status_code == 200:
    parsering = bs(page.text, "html.parser")
    images = parsering.findAll("img")
    for i in images:
        wget.download(url+i["src"])
else:
    print("Response not found.", "HTTP status code = ", page.status_code)