from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/postgres")
Session = sessionmaker(bind=engine)
Base = declarative_base()


# def get_session():
#     engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/postgres")
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     return session


def create_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

