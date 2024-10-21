# pip install requests
import requests
import telebot
from telebot import types
bot = telebot.TeleBot("YOUR TOKEN HERE")

def weather(city="Tashkent"):
    API_KEY = "YOUR TOKEN HERE"
    url = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=ru")
    data = url.json()
    return data


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    btn = types.InlineKeyboardButton('Obhavo qalay ?',callback_data="weather")
    rpl_keyboard = types.InlineKeyboardMarkup()
    rpl_keyboard.add(btn)
    bot.send_message(message.chat.id, "Nima gap obhavo haqida bilishni hohlaysanmi?",reply_markup=rpl_keyboard)

@bot.callback_query_handler(func=lambda call: call.data == "weather")
def handle_weather(call):
    data = weather()

    if data:  
        status = data['weather'][0]["description"]
        temp = data["main"]["temp"]
        city = data["name"]
        celsius = round(temp - 273.15,2)
        response = f"Ob-havo {city}: {celsius}°C,\n{status}"
        bot.send_message(call.message.chat.id, response)
    else:
        bot.send_message(call.message.chat.id, "Ob-havo ma'lumotini olishda xatolik!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    data = weather(message.text.capitalize())
    if data:  
        status = data['weather'][0]["description"]
        temp = data["main"]["temp"]
        celsius = round(temp - 273.15,2)
        city = data["name"]
        response = f"Ob-havo {city}: {celsius}°C,\n{status}"
        bot.send_message(message.chat.id, response)
    else:
        bot.send_message(message.chat.id, "Ob-havo ma'lumotini olishda xatolik!")


bot.infinity_polling()
