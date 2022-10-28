from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from erp import Config, bcrypt
from erp.models.service import User


# create all schemas
def _create_schemas(db):
    db.session.execute('CREATE SCHEMA IF NOT EXISTS service')
    db.session.execute('CREATE SCHEMA IF NOT EXISTS store')
    db.session.commit()


# for root user creation, if we don't have one
def _create_superuser(db):
    # if we don't have superuser user still
    if not User.query.filter_by(username=Config.APP_PASSWORD).first():
        hashed_password = bcrypt.generate_password_hash(Config.APP_PASSWORD).decode('utf-8')
        user = User(username=Config.APP_PASSWORD
                    , email=Config.APP_USER_MAIL
                    , type = 'superuser'
                    , password = hashed_password)
        db.session.add(user)
        db.session.commit()


# for db initialization
def init_db(app, db):
    app.app_context().push()
    _create_schemas(db=db) # create schemas at first
    db.create_all() # create tables
    _create_superuser(db=db) # insert user into table

