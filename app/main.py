from models.base import Base

def main():
    from sqlalchemy import create_engine
    engine = create_engine("sqlite://", echo=True)

    Base.metadata.create_all(engine)

    print('Hello World!')


if __name__ == '__main__':
    main()

