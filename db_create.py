from migrate.versioning import api
from app import app
from app import db
import os.path
db.drop_all()
db.create_all()
if not os.path.exists(app.config['SQLALCHEMY_MIGRATE_REPO']):
    api.create(app.config['SQLALCHEMY_MIGRATE_REPO'], 'bgoapp')
    api.version_control(app.config['SQLALCHEMY_DATABASE_URI'], app.config['SQLALCHEMY_MIGRATE_REPO'])
else:
    api.version_control(app.config['SQLALCHEMY_DATABASE_URI'], app.config['SQLALCHEMY_MIGRATE_REPO'], api.version(app.config['SQLALCHEMY_MIGRATE_REPO']))
