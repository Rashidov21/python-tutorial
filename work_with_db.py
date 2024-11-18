import sqlite3

def get_students():
    con = sqlite3.connect("students_info.db", check_same_thread=False)
    cur = con.cursor()
    
    try:
        cur.execute("SELECT * FROM students")
        return cur.fetchall()
    except sqlite3.DatabaseError as e:
        print(e)

stdudents = get_students()


    