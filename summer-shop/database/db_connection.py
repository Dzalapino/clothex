"""
File to connect to the SQLite database and create the tables
"""
from sqlmodel import SQLModel, Session, create_engine

# Connect to the SQLite database
DB_URL = "sqlite:///./summer.db"
engine = create_engine(DB_URL)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        return session
