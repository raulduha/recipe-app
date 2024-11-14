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
origins = ["http://localhost:8000"]
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

# Servir archivos estáticos
app.mount("/static", StaticFiles(directory="build/static"), name="static")

# Ruta para servir la aplicación React
@app.get("/")
async def serve_frontend():
    return FileResponse("build/index.html")

# Crear tablas al iniciar la aplicación
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
