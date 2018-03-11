import imp
from migrate.versioning import api
from app import db
from config import SQLALCHEMY_MIGRATE_REDO
from config import SQLALCHEMY_DATABASE_URI
migrate=SQLALCHEMY_MIGRATE_REDO\
        +'/versions/%03d_migration.py'%(api.db_version
    (SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REDO)+1)
tmp_module=imp.new_module('old_model')
old_model=api.create_model(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REDO)
exec old_model in tmp_module._dict_script
=api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REDO,
                                  tmp_module.meta,db.metadata)
open(migration,"wt").write(script)
api.upgrade(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REDO)
print 'New migrate saves as'+migration
print 'Current database version:'+str(api.db_version(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REDO))