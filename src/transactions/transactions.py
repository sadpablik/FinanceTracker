from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .models import Transaction
from .schemas import TransactionCreate
from ..database import get_db

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)

@router.post("/")
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    db_transaction = Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    return {"message": "Transaction Created"}
