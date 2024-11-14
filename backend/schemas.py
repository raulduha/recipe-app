from pydantic import BaseModel
from typing import List, Optional

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str


class IngredientDetail(BaseModel):
    ingredient_id: int
    unit_id: int
    quantity_id: int

class RecipeCreate(BaseModel):
    title: str
    description: str
    ingredients: List[IngredientDetail]  # ingredients should be a list of strings
    id: int
    owner_id: int

class IngredientResponse(BaseModel):
    name: str
    unit_id: int
    quantity_id: int
    
class RecipeResponse(RecipeCreate):
    id: int
    owner_id: int
    ingredients: List[IngredientResponse]
