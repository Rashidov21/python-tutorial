import os
import json
import telebot
# Bot tokenini kiriting
API_TOKEN = ""
bot = telebot.TeleBot(API_TOKEN)
# /start komandasi uchun handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Men sizning Telegram botingizman.")

users = []

# Faylni tekshirish va mavjud bo'lsa, o'qish
if os.path.exists("bot_users.json"):
    with open("bot_users.json", "r") as f:
        users = json.load(f)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    user = {
        "id": message.from_user.id,
        "first_name": message.from_user.first_name,
        "last_name": message.from_user.last_name,
        "username": message.from_user.username
    }
    
    # Foydalanuvchini ro'yxatga qo'shish
    if user["id"] not in [u["id"] for u in users]:
        users.append(user)
        with open("bot_users.json", "w") as f:
            json.dump(users, f)
        bot.reply_to(message, "Siz muvaffaqiyatli ro'yxatdan o'tdingiz!")
    else:
        bot.reply_to(message, "Siz oldin yozgansiz!")

    bot.reply_to(message, message.text)

# Botni ishga tushirish
bot.polling()