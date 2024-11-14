from passlib.context import CryptContext
from sqlalchemy.orm import Session
from models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_user(db: Session, username: str, password: str):
    hashed_password = get_password_hash(password)
    new_user = User(username=username, password_hash=hashed_password, role="user")
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # Esto asegura que obtengamos el objeto actualizado de la base de datos
    return new_user  # Asegúrate de retornar el objeto User


def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if user and verify_password(password, user.password_hash):
        return user
    return None
