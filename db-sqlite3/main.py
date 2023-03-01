import sqlite3

con = sqlite3.connect('db-sqlite3/first_db.db', check_same_thread=False) # db ga ulanish obyekt namunasi
cur = con.cursor() # boshqarish obyekti

# print(cur.execute("SELECT * FROM staff").fetchall())

try:
    data = cur.execute(
        """
        SELECT name, age , payment FROM students
        WHERE age >= 16 AND paymentl='true';
        """)
except sqlite3.DatabaseError as error:
    print(error)
else:
    print(data.fetchall())

 # hamma resultni olish
# print(data.fetchone()) # bitta , birinchi natijani olish
# print(data.fetchmany()) # bir nechtasini olish
# print(dir(data))
 # [('Dovudbek', 17, 'true'), ('Nazirillo', 17, 'true'), ('Xurshidbek', 17, 'true')]