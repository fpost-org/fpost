# coding=utf-8
import psycopg2
import psycopg2.extras
import getconf

class DB:    

    def __init__(self):
        config = getconf.ConfigGetter('fpost', ['./app/config.ini', './app/settings.ini'])
        self.__db = config.get('db.db', '')
        self.__host = config.get('db.host', '')
        self.__user = config.get('db.user', '')
        self.__pas = config.get('db.pas', '')
    
    def __str__(self):
        return '[Connection to data base: %s, %s]' % (self.__host, self.__db)
        
    @staticmethod
    def check(self):
        try:
            conn = psycopg2.connect(database=self.__db, user=self.__user, host=self.__host, password=self.__pas)
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
    def insert(self, title, name, text):
        conn = psycopg2.connect(database=self.__db, user=self.__user, host=self.__host, password=self.__pas)
        cursor = conn.cursor()
        sql = "INSERT INTO post(title, name, text) VALUES ('" + title + "', '" + name + "', '" + text + "')"
        try:
            cursor.execute(sql)
            conn.commit()
            return True
        except psycopg2.Error as err:
            return False
        
    @staticmethod
    def getpostbyname(self, name):
        conn = psycopg2.connect(database=self.__db, user=self.__user, host=self.__host, password=self.__pas)
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