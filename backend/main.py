# main.py
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from routers import auth, recipes
from database import get_db, Base, engine

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth")
app.include_router(recipes.router, prefix="/recipes")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Recipe API"}

# Add your DB model creation logic here, if necessary
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)  # Create the tables if they don't exist
