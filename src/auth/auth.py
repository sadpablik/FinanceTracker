from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.auth.models import User 
from src.auth.schemas import UserCreate
from src.database import get_db
from src.core.config import get_security
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from passlib.context import CryptContext


router = APIRouter(prefix="/auth", tags=["Authentication"])


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash_password(password: str) -> str:
    return pwd_context.hash(password)


@router.post("/register")
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == user.email))
    if result.scalar():
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = User(email=user.email, password=hash_password(user.password))
    db.add(new_user)
    await db.commit()
    return {"message": "User registered"}


@router.post(
    "/login",
    response_model=dict,
    summary="User login",
    description="Authenticate user and return access token"
)
def login(username: str, password: str):
    token = get_security().create_access_token(data={"sub": username})
    return {"access_token": token, "token_type": "bearer"}