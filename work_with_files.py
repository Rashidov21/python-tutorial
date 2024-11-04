# import os
# import json
# import telebot

# API_TOKEN = "6145009119:AAHU4Jz3rws0InM66eqXt0BQ_M3pUO3doPg"
# bot = telebot.TeleBot(API_TOKEN)

# # Foydalanuvchilar ro'yxatini saqlash uchun
# users = []

# # Faylni o'qish yoki agar bo'sh bo'lsa, bo'sh massivga almashtirish
# if os.path.exists("bot_users.json"):
#     try:
#         with open("bot_users.json", "r") as f:
#             users = json.load(f)  # JSON o'qish
#     except json.JSONDecodeError:
#         # Agar fayl bo‘sh yoki yaroqsiz bo‘lsa, bo‘sh massivni yozib qo‘yamiz
#         users = []
#         with open("bot_users.json", "w") as f:
#             json.dump(users, f, ensure_ascii=False, indent=4)
# else:
#     # Fayl mavjud bo'lmasa, bo'sh massiv yozib yangi fayl yaratamiz
#     with open("bot_users.json", "w") as f:
#         json.dump(users, f, ensure_ascii=False, indent=4)

# def find_user_by_id(user_id):
#     for user in users:
#         if user["id"] == user_id:
#             return user
#     return None

# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     user = find_user_by_id(message.from_user.id)
#     if user:
#         bot.reply_to(message, f"Salom, {user['first_name']}! Siz allaqachon ro'yxatdan o'tgansiz.")
#     else:
#         bot.reply_to(message, "Salom! Ro'yxatdan o'tish uchun ismingizni kiriting.")

# @bot.message_handler(func=lambda message: True)
# def register_user(message):
#     user = find_user_by_id(message.from_user.id)
#     if user:
#         bot.reply_to(message, f"Siz allaqachon ro'yxatdan o'tgansiz, {user['first_name']}!")
#     else:
#         new_user = {
#             "id": message.from_user.id,
#             "first_name": message.from_user.first_name,
#             "last_name": message.from_user.last_name,
#             "username": message.from_user.username
#         }
#         users.append(new_user)
#         with open("bot_users.json", "w") as f:
#             json.dump(users, f, ensure_ascii=False, indent=4)
#         bot.reply_to(message, f"Xush kelibsiz, {message.text}! Siz muvaffaqiyatli ro'yxatdan o'tdingiz.")

# def bulk_message():

#     msg = """<b>Guido van Rossum</b><i>
#         Guido van Rossum is a Dutch programmer best known as the creator of the Python programming language, first released in 1991. 
#         </i>"""
#     with open("bot_users.json", "r") as f:
#         users = json.load(f) 
#         for user in users:
#             bot.send_photo()
#             bot.send_message(user["id"], "https://avatars.mds.yandex.net/i?id=76028d68c11943fe250f2e4ee59d6d92_l-9231415-images-thumbs&n=13")
#             bot.send_message(user["id"], msg, parse_mode="HTML")
# bulk_message()

# bot.polling()

# try:
#     with open("large_text.txt" ,"r") as file:
#         words = file.read().split(" ")
#         result = []
#         for word in words:
#             result.append(f"{word} : {words.count(word)}")
#         for i in sorted(set(result)):
#             with open("result_text.txt", "a+") as f:
#                 f.write(f"{i}\n")
# except Exception as er:
#     print(er)

# Masala: mahsulotlar.txt faylida har bir qatorga mahsulot nomi va uning narxi, masalan, Olma, 5000 shaklida yozilgan. Barcha mahsulotlar narxini o‘qing va o‘rtacha narxni hisoblang.
# input:
# Olma : 5000
# Anor : 3000
# Tarvuz : 4000

# output:
# Natija: 4000 (masalan)
# try:
#     with open("products.txt", "r") as file:
#         summ = 0
#         data = file.readlines()
#         for i in data:
#             summ += int(i.split(":")[1])
#             print(summ)
#         print("Ortacha summa = ", summ / len(data))
# except Exception as e:
#     print(e)

#  Masala: uchrashuvlar.txt faylida har bir qatorga bir kunga bir uchrashuv va uning vaqti yozilgan (masalan, 2023-10-25, 14:00, Muhim yig‘ilish). Bugungi kunga tegishli barcha uchrashuvlarni bugun.txt fayliga yozing.
#    - Natija: bugun.txt faylida bugungi kun uchrashuvlari.

# input :2023-10-25, 14:00, Muhim yig‘ilish
# from datetime import datetime 
# # joriy sanani olish
# current_date = datetime.now().date()
# try:
#     with open("input.txt","r") as file:
#         dates = file.readlines()
#         for note in dates:
#             line = note.split(",")[0]
#             if len(line.split("-")) == 3:
#                 year = int(line.split("-")[0])
#                 month = int(line.split("-")[1])
#                 day = int(line.split("-")[2])
#                 note_date = datetime(year, month, day).date()
          
#                 print("Currunt date = ", current_date)
#                 print("Note date = ", note_date)
#             else:
#                 print("False")
#                 continue
# except Exception as e:
#     print(e)

# import json 

# with open("cities.json", "r") as file:
#     cities = json.load(file)
#     print([city["name"] for city in list(filter(lambda x: x["population"] > 500000, cities))])
# import os 

# print(dir(os))
# print(os.getcwd()) # fayl joriy direktoriyasi 
# print(os.listdir()) # direktoriya ichidagi narsalar royhati 
# os.path - direktoriya bilan ishlash uchun 
# print(os.path.abspath("products.txt")) # fayl uchun toliq manzil
# s = os.path.abspath("products.txt")
# print(os.path.dirname(s)) # papka manzili
# print(os.path)