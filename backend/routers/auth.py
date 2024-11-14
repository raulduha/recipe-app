from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas import UserCreate, UserResponse
from services import create_user, authenticate_user
from models import User  # Importing the User model from models.py
from database import get_db  # Importing the database session dependency

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists in the database
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")
    
    # Create new user
    new_user = create_user(db, user.username, user.password)
    return new_user

@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    # Authenticate user using the provided username and password
    authenticated_user = authenticate_user(db, user.username, user.password)
    if not authenticated_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return {"message": "Logged in successfully", "user": authenticated_user}
