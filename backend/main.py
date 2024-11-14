# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routers import auth, recipes
from database import Base, engine
import os

app = FastAPI()

# Configurar CORS
origins = ["http://localhost:8000", "https://recipe-app-ikm1.onrender.com"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Montar archivos estáticos
static_path = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_path), name="static")

# Incluir routers
app.include_router(auth.router, prefix="/auth")
app.include_router(recipes.router, prefix="/recipes")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Recipe API"}

# Crear tablas al iniciar la aplicación
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)