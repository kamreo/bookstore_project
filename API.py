"""
Program that stores book's informations:
Title, Author, Year, ISBN

User can:
View records,
Search an entry,
Add entry,
Update entry,
Delete entry

"""
import sqlite3

def connect():
    conn=_sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,"
                " title TEXT, author TEXT, year INTEGER, isbn INTEGER )")
    conn.commit()
    conn.close()

def add_entry(title, author, year, isbn):
    conn = _sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view_all():
    conn = _sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def search_entry(title="", author="", year="", isbn=""):
    conn = _sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn = _sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    rows=cur.fetchall()
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn = _sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    rows = cur.fetchall()
    conn.commit()
    conn.close()

connect()