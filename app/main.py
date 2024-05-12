
from app.models.base import Base
from app.settings import Settings
from app.models.store import Client


def main():

    Base.init_database()

    from sqlalchemy.orm import Session

    with Session(Base.get_engine()) as session:
        client = Client(id=1)
        session.add(client)
        session.commit()


if __name__ == '__main__':
    main()

