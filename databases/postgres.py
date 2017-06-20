import psycopg2

def create_table():
    #Connect to a db - this line will build a db if you dont have a db file yet
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    #Then we create a cursor
    cur=conn.cursor()
    #Real means a float
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

    #Then we commit
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    #cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", ('Wine', 10, 22))
    conn.commit()
    conn.close()

def delete(item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    #Item needs a comma after
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

def view():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

create_table()
