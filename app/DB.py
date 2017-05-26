# coding=utf-8
import psycopg2
import psycopg2.extras
import random
import string

class DB:    
    db = 'fpost'
    user = 'postgres'
    host = 'localhost'
    pas = 'secret'
    
    @staticmethod
    def check():
        try:
            conn = psycopg2.connect(database=DB.db, user=DB.user, host=DB.host, password=DB.pas)
        except psycopg2.Error as err:
            return False
            
        sql = "SELECT * FROM post LIMIT 1"
        
        try:
            cur = conn.cursor()
            cur.execute(sql)
            return True
        except psycopg2.Error as err:
            return False

    @staticmethod
    def insert(title, name, text):
        conn = psycopg2.connect(database=DB.db, user=DB.user, host=DB.host, password=DB.pas)
        cursor = conn.cursor()
        sql = "INSERT INTO post(title, name, text) VALUES ('" + title + "', '" + name + "', '" + text + "')"
        cursor.execute(sql)
        conn.commit()
        return True
        
    @staticmethod
    def getpostbyname(name):
        conn = psycopg2.connect(database=DB.db, user=DB.user, host=DB.host, password=DB.pas)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM post WHERE title = '" + name + "'")
        row = cursor.fetchone()
        return row
    
    @staticmethod
    def create_db():
        conn = psycopg2.connect(database=DB.db, user=DB.user, host=DB.host, password=DB.pas)
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS post (title varchar, name varchar, text varchar)")
        conn.commit()
        c.close()
        conn.close()
        return True
    
    @staticmethod
    def re_title(name):
        conn = psycopg2.connect(database=DB.db, user=DB.user, host=DB.host, password=DB.pas)
        c = conn.cursor()
        c.execute("SELECT * FROM post WHERE title = '" + name + "' LIMIT 1;")
        counts = c.rowcount
        c.close()
        conn.close()
        if counts > 0:
            return True
        else:
            return False
    
    @staticmethod
    def check_title(name):
        conn = psycopg2.connect(database=DB.db, user=DB.user, host=DB.host, password=DB.pas)
        c = conn.cursor()
        c.execute("SELECT * FROM post WHERE title = '" + name + "' LIMIT 1;")
        counts = c.rowcount
        c.close()
        conn.close()
        if counts > 0:
            new_title = name +'-'+ DB.random_string(7)
            return DB.check_title(new_title)
        else:
            return name
    
    def random_string(length):
        pool = string.ascii_lowercase + string.digits
        return ''.join(random.choice(pool) for i in range(length))