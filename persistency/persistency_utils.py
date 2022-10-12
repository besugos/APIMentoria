from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_session():
    engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/postgres")
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
