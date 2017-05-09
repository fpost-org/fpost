import unittest
import hmac, hashlib
import random
import sys 
from builtins import str
sys.path.append("..")
from app.DB import DB

class TestDB(unittest.TestCase):
    def testInsert(self):
        title = hmac.new(bytearray('signature','utf-8'), bytearray(str(random.random()),'utf-8'), hashlib.sha256).hexdigest()
        name = hmac.new(bytearray('signature','utf-8'), bytearray(str(random.random()),'utf-8'), hashlib.sha256).hexdigest()
        post = hmac.new(bytearray('signature','utf-8'), bytearray(str(random.random()),'utf-8'), hashlib.sha256).hexdigest()
        DB.create_db();
        DB.insert_db(title, name, post)
        res = DB.getpostbyname(title)
        flag = False
        if (res[0]==title and res[1]==name and res[2]==post):
            flag = True
        self.assertTrue(flag)

if __name__ == '__main__':
    unittest.main()