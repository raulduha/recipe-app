from fastapi import APIRouter, HTTPException
from schemas import UserCreate, UserResponse
from services import create_user, authenticate_user
from models import users_db
router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate):
    existing_user = next((u for u in users_db if u["username"] == user.username), None)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")
    new_user = create_user(user.username, user.password)
    return new_user

@router.post("/login")
def login(user: UserCreate):
    authenticated_user = authenticate_user(user.username, user.password)
    if not authenticated_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Logged in successfully", "user": authenticated_user}
