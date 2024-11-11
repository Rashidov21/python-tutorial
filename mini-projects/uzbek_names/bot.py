# pip install telebot
import telebot
from telebot import types
from db import get_name


API_KEY = "6145009119:AAF0CFhS-zP2DlvjRoqoUT-4RwbmoMKlcew"
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id,"Salom , ism yozing !")    
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    name = get_name(message.text)
    if isinstance(name, tuple):
        msg = f"<b>{name[1]}</b>\n<i>{name[2]}</i>"
        bot.send_message(message.chat.id,msg , parse_mode="HTML")
    else:
        bot.send_message(message.chat.id, "Ism topilmadi")
    

bot.infinity_polling()