from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from src.database import Base
from sqlalchemy.ext.declarative import declarative_base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True,index=True)
    username = Column(String,unique=True)
    email = Column(String,unique=True)
    hashed_password = Column(String)
