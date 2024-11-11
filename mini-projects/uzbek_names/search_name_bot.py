import telebot
import requests
from bs4 import BeautifulSoup

API_KEY = ""
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id,"Salom , ism yozing !")
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    url = "https://ismlar.com/search/"+message.text
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    names_block = soup.find("ul", class_="list-none space-y-2")
    name_block = names_block.findAll("li")[:3]
    if name_block:
        for name in name_block:
            n = name.h2.text.strip()
            d = name.find("div", class_="space-y-4").text.strip()
            bot.send_message(message.chat.id, f"<b>{n}</b>\n<i>{d}</i>", parse_mode="HTML")
    else:
        bot.send_message(message.chat.id, "Ism topilmadi")
bot.infinity_polling()