from fastapi import FastAPI
from routers import auth, recipes

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(recipes.router, prefix="/recipes")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Recipe API"}
