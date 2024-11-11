import sqlite3
# sql = """
# CREATE TABLE names(
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name TEXT,
#     description TEXT);
# """
def db_write(id,name,description):
    con = sqlite3.connect("names.db", check_same_thread=False)
    cur = con.cursor()
    sql = f"INSERT INTO names VALUES({id},'{name}','{description}');"
    try:
        cur.execute(sql)
    except sqlite3.DatabaseError as e:
        print(e)
    else:
        con.commit()
        print("Success !")
        
def get_last_item_id():
    con = sqlite3.connect("names.db", check_same_thread=False)
    cur = con.cursor()
    sql = "SELECT id FROM names ORDER BY id DESC LIMIT 1;"
    cur.execute(sql)
    return cur.fetchone()[0]
