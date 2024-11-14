# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, recipes
from database import Base, engine

app = FastAPI()

# Configurar CORS
origins = ["http://localhost:3000", "http://recipe-app"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
