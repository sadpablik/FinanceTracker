from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from src.database import Base

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True,index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Float)
    category = Column(String)
    date = Column(DateTime)
    type = Column(String)
    description = Column(String, nullable=True)

