from flask import Flask
app = Flask(__name__)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app.config.from_object('config')
app.config['SECRET_KEY'] = 'mtianyan_movie'
db=SQLAlchemy(app)


import os
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir

Im=LoginManager()
Im.init_app(app)
oid=OpenID(app,os.path.join(basedir,'tmp'))
Im.login_view='login'

from config import basedir,ADMINS,MAIL_SERVER,MAIL_PORT,MAIL_USERNAME,MAIL_PASSWORD

if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    credentials=None
    if MAIL_USERNAME or MAIL_PASSWORD:
        credentials=(MAIL_USERNAME,MAIL_PASSWORD)
        mail_handler=SMTPHandler((MAIL_SERVER,MAIL_PORT).'no-reply@'+MAIL_SERVER,ADMINS,'microblog failure',credentials)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)


if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler=RotatingFileHandler('tmp/microblog.log','a',1*1024*1024,10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('microblog startup')

