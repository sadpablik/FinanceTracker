from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from src.database import Base
from sqlalchemy.ext.declarative import declarative_base


class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True,index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Float)
    category = Column(String)
    date = Column(DateTime)
    type = Column(String)
    description = Column(String, nullable=True)