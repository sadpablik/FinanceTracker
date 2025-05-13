from pydantic import BaseModel
from datetime import datetime

class TransactionCreate(BaseModel):
    amount: float
    category: str
    type: str
    description: str  | None = None