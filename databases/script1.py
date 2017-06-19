import sqlite3

def create_table():
    #Connect to a db - this line will build a db if you dont have a db file yet
    conn=sqlite3.connect("lite.db")
    #Then we create a cursor
    cur=conn.cursor()
    #Real means a float
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    cur.execute("INSERT INTO store VALUES ('Wine Glass', 8, 10.5)")
    #Then we commit
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))
    conn.commit()
    conn.close()

insert("Water Glass", 10, 5)

def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

print(view())
