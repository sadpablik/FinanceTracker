from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..auth.models import User
from ..auth.schemas import UserCreate
from ..database import get_db
from authx import AuthXConfig
from src.core.config import get_security

router = APIRouter()
config = AuthXConfig()



@router.post("/register")
def register(user: UserCreate,db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = "fale_hashed_ " + user.password
    new_user = User(username=user.username,email=user.email,hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    return {"message": "User registered"}

@router.post("/login")
def login(username: str, password:str):
    token = get_security.create_access_token(data = {"sub": username})

