from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, recipes

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Permitir el origen del frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth")
app.include_router(recipes.router, prefix="/recipes")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Recipe API"}