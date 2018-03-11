from migrate.versioning import api
from config import SQLALCHEMY_MIGRATE_REDO
from config import SQLALCHEMY_DATABASE_URI
v=api.db_version(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REDO)
api.downgrade(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REDO,v-1)
print 'Current database version:'+str(api.db_version(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REDO))