from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..transactions.models import Transaction
from ..transactions.schemas import TransactionCreate
from ..database import  get_db


router = APIRouter()
@router.post("/transactions")
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    db_transaction = Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    return {"message": "Transaction Created"}

