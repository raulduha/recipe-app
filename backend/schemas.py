from pydantic import BaseModel
from typing import List, Optional

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str

class RecipeCreate(BaseModel):
    title: str
    description: str
    ingredients: str

class RecipeResponse(RecipeCreate):
    id: int
    owner_id: int
