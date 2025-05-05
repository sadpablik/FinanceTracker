from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
SQL_DATABASE = f"{os.getenv('DATABASE_URL')}"
engine = create_engine(SQL_DATABASE)
Session = sessionmaker(autocommit = False,bind=engine,autoflush = False)
Base = declarative_base()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()