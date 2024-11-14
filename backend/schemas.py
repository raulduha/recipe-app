from pydantic import BaseModel
from typing import List, Optional

# Esquema para la creación de usuarios
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
    owner_id: int
    ingredients: List[IngredientDetail]


class IngredientResponse(BaseModel):
    ingredient_id: int
    unit_id: int
    quantity_id: int
    name: str
    unit: str
    quantity: float

class RecipeResponse(BaseModel):
    id: int
    title: str
    description: str
    owner_id: int
    ingredients: List[IngredientResponse]

# Esquema para la respuesta de unidades de medida
class UnitResponse(BaseModel):
    id: int
    unit: str

    class Config:
        orm_mode = True

# Esquema para la respuesta de cantidades
class QuantityResponse(BaseModel):
    id: int
    quantity: float

    class Config:
        orm_mode = True
