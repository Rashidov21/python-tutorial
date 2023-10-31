import sqlite3
import time
from faker import Faker
# Data base tutorial : sqlite3

con = sqlite3.connect("./main.db", check_same_thread=False) # bu db ga bog'lanish 
cur = con.cursor() # db boshqarish obyekti

sql1 = """CREATE TABLE students(
    name TEXT,
    age INTEGER,
    gender TEXT,
    point INTEGER
    );"""
    
fake = Faker()    
# try:
#     sql4 = """DELETE FROM students WHERE name='Danielle Ford'"""
#     cur.execute(sql4)
# except sqlite3.DatabaseError as er:
#     print(er)
# else:
#     # time.sleep(1)
#     print("Success !")
#     con.commit() 

# for i in range(10):
    
#     sql2 = f"""INSERT INTO students(name,age,gender,point)
#     VALUES('{fake.name()}',{fake.random_int(6,19)},'male',{fake.random_int(30,100)});"""
#     # hammasini olish
#     sql3 = """SELECT * FROM students"""
#     # point < 90 
#     # sql3 = """SELECT * FROM students WHERE point < 90"""
#     sql4 = """DELETE FROM students WHERE name='Danielle Ford'"""
#     try:
#         data = cur.execute(sql3)
#     except sqlite3.DatabaseError as er:
#         print(er)
#     else:
        
#         # time.sleep(1)
#         print("Success !")
#         con.commit() # o'zgarishlarni tasdiqlash
        
        # print(data.fetchone())
        # for data in data.fetchall():
        #     print(data)
# con.close() # boshqaruvchi yakunlash
con.close() # bog'lnishni yakunlash