from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from erp import Config


# create all schemass
def create_schemas(db):
    db.session.execute('CREATE SCHEMA IF NOT EXISTS service')
    db.session.execute('CREATE SCHEMA IF NOT EXISTS main')
    db.session.execute('CREATE SCHEMA IF NOT EXISTS store')
    db.session.commit()


# for db initialization, when we stil don't have one
def init_db(app, db):
    app.app_context().push()
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
    if not database_exists(engine.url):
        create_database(engine.url) 
    create_schemas(db=db)
    db.create_all()