
import requests
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'your token'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def get_movie_poster(query:str):
    url = "rapid url"

    querystring = {"q":query}

    headers = {
        "X-RapidAPI-Key": "your key",
        "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    url = data["d"][0]["i"]["imageUrl"]
    return url

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm MoviePosterBot!\nPowered by me.")



@dp.message_handler()
async def echo(message: types.Message):
    # print(message.from_user)
    url = get_movie_poster(message.text)
    await message.answer(url)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


# import time
# import telepot
# from telepot.loop import MessageLoop

# def handle(msg):
#     content_type, chat_type, chat_id = telepot.glance(msg)
#     # print(content_type, chat_type, chat_id)
    
#     if content_type == 'text':
#         if msg["text"].lower() == "salom":
#             bot.sendMessage(chat_id, "salom")
#         else:
#             bot.sendMessage(chat_id, "Salom ber !")

#  # get token from command-line

# bot = telepot.Bot(token="6145009119:AAExs6OT4pjlV-34sMCgRhvhB_Xi9SMlmJE")
# MessageLoop(bot, handle).run_as_thread()
# print ('Listening ...')

# Keep the program running.
# while 1:
#     time.sleep(10)

