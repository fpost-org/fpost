import unittest
import hmac, hashlib
import random
import sys
sys.path.append("..")
from app.DB import DB

class TestDB(unittest.TestCase):
    def testDbInsert(self):
        title = hmac.new(bytearray('signature','utf-8'), bytearray(str(random.random()),'utf-8'), hashlib.sha256).hexdigest()
        name = hmac.new(bytearray('signature','utf-8'), bytearray(str(random.random()),'utf-8'), hashlib.sha256).hexdigest()
        post = hmac.new(bytearray('signature','utf-8'), bytearray(str(random.random()),'utf-8'), hashlib.sha256).hexdigest()
        flask_db = DB()
        DB.load_config(flask_db,['../app/config.ini'])
        DB.create_db(flask_db);
        DB.insert(flask_db, title, name, post)
        res = DB.getpostbyname(flask_db, title)
        flag = False
        if (res[0]==title and res[1]==name and res[2]==post):
            flag = True
        self.assertTrue(flag)
     
    def testDbCheck(self):
        flask_db = DB()
        DB.load_config(flask_db,['../app/config.ini'])
        flag = DB.check(flask_db)
        self.assertTrue(flag)
     
if __name__ == '__main__':
    unittest.main()