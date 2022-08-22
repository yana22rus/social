import sqlite3



connection = sqlite3.connect('id_users.db',check_same_thread=False)


cursor = connection.cursor()

with sqlite3.connect("id_users.db") as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT UNIQUE,
    hash_password TEXT,
    email TEXT UNIQUE,
    time_registration TEXT
    )""")