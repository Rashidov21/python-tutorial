import os
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F

from config.token import API_TOKEN
from config.config import get_data
# Объект бота
bot = Bot(token=API_TOKEN)
# Диспетчер
dp = Dispatcher()

@dp.message(F.text.lower() == "musiqa qidirish")
async def search_music(message: types.Message):
    await message.answer("Musiqa nomini yozing...")
    
@dp.message(F.text.lower() == "qo'shiqchi qidirish")
async def search_artist(message: types.Message):
    await message.answer("Musiqa nomini yozing...")


@dp.message(F.text)
async def search(message: types.Message):
    await message.answer(get_data(message.text), parse_mode='HTML')
   

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Musiqa qidirish"),
            types.KeyboardButton(text="Qo'shiqchi qidirish")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Iltimos tanlang"
    )
    await message.answer("Nimani qidiramiz ?", reply_markup=keyboard)















# import requests
# query = "ozodbek"
# data = requests.get(f"https://api.deezer.com/search?q={query}")
# # print(len()
# for music in data.json()["data"]:
#     # print(music["id"])
#     # print(music["rank"])
#     print(music["title"])
#     print(music["artist"]["name"])
#     print(music["artist"]["picture"])