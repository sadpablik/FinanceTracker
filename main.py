from dotenv import load_dotenv
from fastapi import FastAPI
from src.auth.auth import router as auth_router
from src.transactions import transactions
from src.database import engine, Base
from src.core.config import get_security

load_dotenv()

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(auth_router, prefix="/auth")

security = get_security()


app.include_router(transactions.router, prefix="/transactions")

@app.get("/")
def root():
    return {"message": "Personal Finance Tracker API"}