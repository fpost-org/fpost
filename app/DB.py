# coding=utf-8
import sqlite3
import psycopg2
import psycopg2.extras
from pip._vendor.distlib import database

def check_db(db, user, host, pas):
    try:
        conn = psycopg2.connect(database=db, user=user, host=host, password=pas)
    except psycopg2.Error as err:
        return False
            
    sql = "SELECT * FROM post LIMIT 3"
        
    try:
        cur = conn.cursor()
        cur.execute(sql)
        return True
    except psycopg2.Error as err:
        return False

class DB:    
    
    def __init__(self):
        a = ''
  
    db = 'fpost'
    user = 'postgres'
    host = 'localhost'
    pas = 'sxjkjvdfhjw72jKldcjn'                  
    
    sqlitedb = 'my.db'
    conn = ''
    
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
    def insert(title, name, text):
        conn = psycopg2.connect(database=DB.db, user=DB.user, host=DB.host, password=DB.pas)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO post VALUES ("'+title+'", "'+name+'", "'+text+'");')
        conn.commit()
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
        cursor = DB.conn.cursor()
        cursor.execute('SELECT * FROM post WHERE title = "' + name + '"')
        row = cursor.fetchone()
        return row        