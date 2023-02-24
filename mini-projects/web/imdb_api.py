import requests

url = "<url>"

querystring = {"q":"x-men"}

headers = {
	"X-RapidAPI-Key": "<api>",
	"X-RapidAPI-Host": "imdb8.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
data = response.json()
print(data["d"][0]["i"]["imageUrl"])