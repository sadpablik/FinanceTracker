from fastapi import FastAPI
from src.database import init_db
from src.auth.auth import router as auth_router
from src.transactions.transactions import router as transactions_router
from src.core.config import get_security

app = FastAPI(title="Personal Finance Tracker", version="0.1.0")

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)
app.include_router(
    transactions_router,
    prefix="/transactions",
    tags=["Transactions"]
)

@app.on_event("startup")
async def on_startup():
    await init_db()

security = get_security()

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Personal Finance Tracker API"}

@app.get("/test")
async def test():
    return {"message": "Test endpoint"}