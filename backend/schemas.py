from pydantic import BaseModel
from typing import List, Optional

# Esquema para la creación de usuarios
class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
from pydantic import BaseModel
from typing import List, Optional

class IngredientDetail(BaseModel):
    ingredient_id: int
    unit_id: int
    quantity_id: int
    name: Optional[str] = None
    unit: Optional[str] = None
    quantity: Optional[float] = None

class RecipeCreate(BaseModel):
    title: str
    description: str
    ingredients: List[IngredientDetail]
    owner_id: int

class RecipeResponse(BaseModel):
    id: int
    title: str
    description: str
    owner_id: int
    ingredients: List[IngredientDetail]

    class Config:
        orm_mode = True

class IngredientResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class UnitResponse(BaseModel):
    id: int
    unit: str

    class Config:
        orm_mode = True

class QuantityResponse(BaseModel):
    id: int
    quantity: float

    class Config:
        orm_mode = True
