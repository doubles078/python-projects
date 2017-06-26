import sqlite3

class Database:

    def __init__(self):
        self.conn=sqlite3.connect("books.db")
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title text, author text, year INTEGER, isbn INTEGER)")
        self.conn.commit()

    def insert(self, title, author, year, isbn):
        #By inserting a null, python knows that the primary key should be incremented automatically
        self.cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)", (title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        #we want the data returned as a tuple
        rows=self.cur.fetchall()
        return rows

    #Pass empty strings as default values so a user can choose to pass only one argument
    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? or author=? or year=? or isbn=?", (title, author, year, isbn))
        #we want the data returned as a tuple
        rows=self.cur.fetchall()
        return rows

    def delete(self, id):
        #Need a comma after if only one argument
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        #Need a comma after if only one argument
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
