from fastapi import FastAPI
import asyncio
from src.database import init_db
from src.auth.auth import router as auth_router
from src.transactions import transactions
from src.core.config import get_security

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await init_db()

security = get_security()

@app.get("/")
def root():
    return {"message": "Personal Finance Tracker API"}
