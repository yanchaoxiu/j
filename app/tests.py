import os
import unittest
from config import basedir
from app import app,db
from models import User

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING']=True
        app.config['WTF_CSRF_ENABLED']=False
        app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///***'
        self.app=app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_avatar(self):
        u=User(nickname='John',email='yanchaoxiu@163.com')
        avatar=u.avator(128)
        expected='*****'
        assert avatar[0:len(expected)]==expected

    def test_make_unique_nickname(self):
        u=User(nickname='john',email='yanchaoxiu@163.com')
        db.session.add(u)
        db.session.commit()
        nickname=User.make_unique_nickname('John')
        assert nickname !='john'
        u=User(nickname=nickname,email='susan@163.com')
        db.session.add(u)
        db.session.commit()
        nickname2=User.make_unique_nickname('john')
        assert nickname2 !='john'
        assert nickname2 !=nickname
if __name__=='__main__':
    unittest.main()

