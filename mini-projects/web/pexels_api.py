import requests
import io
from PIL import Image
# import pprint

API = "AO5zZivgo9rnloJr590042Ferd3RDNWTGP9xB0SUvZLw2CrVXlNdD7a9"

def download(q, count):
    i = 1
    while i <= int(count): 
        PARAMS = {"page":f"{i}"}
        HEADERS = {
            "Authorization":"AO5zZivgo9rnloJr590042Ferd3RDNWTGP9xB0SUvZLw2CrVXlNdD7a9"
        }
        url = f"https://api.pexels.com/v1/search?query={q}&per_page=1"
        
        page = requests.get(url=url, headers=HEADERS, params=PARAMS)
        # print(page.text)
        response = page.json()
        # print(response)
        image_url = response.get("photos")[0].get("src").get("large")
        obj = requests.get(image_url)

        image = Image.open(io.BytesIO(obj.content))
        # print(f"./media/{q}_{i}.jpeg")
        path = "media/" + q + ".jpeg"
        image.save(path)
        # wget.download(url=image_url, out=f"./media/{q}_{i}.{image_url.split('.')[-1]}") # media/fox_1.jgep
        
        i += 1
    # pprint.pprint(page.json())



def main():
    q = input("Query \n:")
    count = input("Count \n:")
    
    download(q,count)
main()