from typing import List, Optional
from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base
from sqlalchemy.ext.declarative import declared_attr


class Store(Base):
    __abstract__ = True
    _prefix = __qualname__.lower()

    @declared_attr
    def __tablename__(cls):
        return '_'.join([cls._prefix, cls.__name__.lower()])


class Client(Store):

    id: Mapped[int] = mapped_column(primary_key=True)

