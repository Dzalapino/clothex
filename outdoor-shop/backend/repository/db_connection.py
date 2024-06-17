import os
from sqlmodel import Session, create_engine

# Connect to the SQLite database
DB_URL = "sqlite:///./test.db"
engine = create_engine(DB_URL)

def delete_db():
    if os.path.exists('test.db'):
        os.remove('test.db')
        print("Database dropped successfully.")
    else:
        print("Database file not found.")

def get_session():
    with Session(engine) as session:
        return session