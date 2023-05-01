from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///db/db.sqlite')


def get_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


Base = declarative_base()
