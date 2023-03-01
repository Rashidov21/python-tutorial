"""
Download all images from  emoji.wannathis.one home page
"""
import sqlite3
import requests
import wget
from bs4 import BeautifulSoup as bs

url = "https://namozvaqti.uz/oylik/3/andijon"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

def connect_to_db():
    con = sqlite3.connect('mini-projects/web/namaz_times.db', check_same_thread=False)
    return con
# con = connect_to_db()
# con.cursor().execute(
#     """
#     CREATE TABLE times(
#         date TEXT,
#         weekday TEXT,
#         fajr TEXT,
#         sunrise TEXT,
#         duhr TEXT,
#         asr TEXT,
#         maghrib TEXT,
#         isha TEXT);
#     """
# )

page = requests.get(url=url)
print(page.status_code) # if 200 its ok

if page.status_code == 200:
    parsering = bs(page.text, "html.parser")
    times = parsering.findAll("tr")
    con = connect_to_db()
    for i in times[1:]:
        day = [x.text for x in i.findAll("td")]         
        try:
            cur = con.cursor()
            cur.execute(
            f"""
            INSERT INTO times
            VALUES('{day[0].split(" ")[0]}', '{day[0].split(" ")[1]}',
            '{day[1]}','{day[2]}','{day[3]}','{day[4]}','{day[5]}','{day[6]}');
            """
            )
        except sqlite3.DatabaseError as e:
            print(e) 
        else:
            con.commit()
         
    else:
        print("The end")
        cur.close()
        con.close()
        


