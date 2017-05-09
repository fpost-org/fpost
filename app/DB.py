# coding=utf-8
import sqlite3

class DB:
    def __init__(self):
        a=1
    
    sqlitedb = 'my.db'    
    
    @staticmethod
    def create_db():
        conn = sqlite3.connect(DB.sqlitedb)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS post (title varchar, name varchar, text varchar)''')
        conn.commit()
        c.close()
        conn.close()
        return True
    
    @staticmethod
    def insert_db(title, name, text):
        conn = sqlite3.connect(DB.sqlitedb)
        rows = [(title, name, text)]
        conn.cursor().executemany("INSERT INTO post VALUES (?,?,?)", rows)
        conn.commit()
        conn.close()
        return True
        
    @staticmethod
    def show_db():
        conn = sqlite3.connect(DB.sqlitedb)
        c = conn.cursor()
        c.execute('SELECT * FROM post')
        row = c.fetchone()
        res = ''
        while row is not None:
            a = "title: " + row[0] + " | name: " + row[1] + " | text: " + row[2] + "<br>"
            res += a
            row = c.fetchone()
        c.close()
        conn.close()
        return res
        
    @staticmethod
    def getpostbyname(name):
        conn = sqlite3.connect(DB.sqlitedb)
        c = conn.cursor()
        c.execute('SELECT * FROM post WHERE title = "' + name + '"')
        row = c.fetchone()
        c.close()
        conn.close()
        return row        