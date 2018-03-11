from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REDO
from app import db
import os.path
db.create_all()
if not os.path.exists(SQLALCHEMY_MIGRATE_REDO):
    api.create(SQLALCHEMY_MIGRATE_REDO,'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REDO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REDO,api.version(SQLALCHEMY_MIGRATE_REDO))