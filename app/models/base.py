from sqlalchemy import orm, create_engine,  MetaData, BigInteger, String
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declared_attr
import os
from app.settings import Settings


class DataBase:

    __abstract__ = True

    metadata = MetaData()
    type_annotation_map = {
        str: String().with_variant(String(255), "mysql", "mariadb"),
    }

    database_path = Settings.database_path

    # @declared_attr
    # def __tablename__(cls):
    #     """Returns table name for end-class, which looks like 'superclass_class' """
    #     return '_'.join([str(cls.__bases__[0].__name__.lower()), cls.__name__.lower()])

    @classmethod
    def get_engine(cls):
        return create_engine(f"sqlite:///{cls.database_path}", echo=True)

    @classmethod
    def init_database(cls):
        engine = cls.get_engine()
        if not database_exists(engine.url):
            os.mkdir(os.path.dirname(cls.database_path))
            create_database(engine.url)
        Base.metadata.create_all(engine)


Base = orm.declarative_base(cls=DataBase)

