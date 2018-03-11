CSRF_ENABLED=True
SERVER_KEY='you will-never-guess'

OPENID_PROVIDERS=[
    {'name':'Google','url':'https://www.goole.com.account/o8/id'},
    {'name':'Yahoo','url':'https://www.goole.com.account/o8/id'},
    {'name':'AOL','url':'https://www.goole.com.account/o8/id'},
    {'name':'Flickr','url':'https://www.goole.com.account/o8/id'},
    {'name':'MyOpenID','url':'https://www.goole.com.account/o8/id'},
]


import os
basedir=os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(basedir,'app.db')
SQLALCHEMY_MIGRATE_REDO=os.path.join(basedir,'db_repository')


#mail server settings
MAIL_SERVER='localhost'
MAIL_PORT=25
MAIL_USERNAME=None
MAIL_PASSWORD=None

# administrator list
ADMINS=['yanchaoxiu@163.com']