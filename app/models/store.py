from typing import List, Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base
from sqlalchemy.ext.declarative import declared_attr


class StoreTable(Base):
    __abstract__ = True
    _prefix = 'store_'

    @declared_attr
    def __tablename__(cls):
        return cls._prefix + cls.__class__.__name__.lower()


class Client(Base):

    id: Mapped[int] = mapped_column(primary_key=True)

