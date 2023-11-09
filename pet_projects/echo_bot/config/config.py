import requests

def get_data(query):
    data = requests.get(f"https://api.deezer.com/search?q={query}")
    title = data.json()["data"][0]["title"]
    artist = data.json()["data"][0]["artist"]["name"]
    artist_image_link = data.json()["data"][0]["artist"]["picture"]

    msg = f"Natijalar \n{artist_image_link}\n<b>Artist : {artist}</b>\n<b>Song : {title}</b>"
    return msg
