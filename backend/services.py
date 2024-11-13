from passlib.context import CryptContext
from typing import Optional
from models import users_db

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_user(username: str, password: str) -> Optional[dict]:
    hashed_password = get_password_hash(password)
    new_user = {"id": len(users_db) + 1, "username": username, "password": hashed_password}
    users_db.append(new_user)
    return new_user

def authenticate_user(username: str, password: str) -> Optional[dict]:
    for user in users_db:
        if user["username"] == username and verify_password(password, user["password"]):
            return user
    return None
