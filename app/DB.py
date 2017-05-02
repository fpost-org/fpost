# coding=utf-8

class DB:
    def __init__(self, exp):
        a=a
        
    
    @staticmethod
    def createDB():
        conn = sqlite3.connect('my.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE post (id int auto_increment primary key, title varchar, name varchar, text varchar)''')
        conn.commit()
        c.close()
        conn.close()
    
    @staticmethod
    def insertDB():
        conn = sqlite3.connect('my.db')
        c = conn.cursor()
        c.execute("INSERT INTO post (title,name,text) VALUES ('post1title','user','text post')")
        conn.commit()
        c.close()
        conn.close()
        
    @staticmethod
    def selectDB():
        conn = sqlite3.connect('my.db')
        c = conn.cursor()
        c.execute('SELECT * FROM post')
        row = c.fetchone()
        while row is not None:
            return("id:"+str(row[0])+" title: "+row[1]+" | name: "+row[2]+" | text: "+row[3])
            row = c.fetchone()
        c.close()
        conn.close()