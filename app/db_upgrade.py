from migrate.versioning import api
from config import SQLALCHEMY_MIGRATE_REDO
from config import SQLALCHEMY_DATABASE_URI
api.upgrade(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REDO)
print 'Current database version:'+str(api.db_version(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REDO))