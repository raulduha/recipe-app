from fastapi import APIRouter, HTTPException
from schemas import RecipeCreate, RecipeResponse
from models import recipes_db

router = APIRouter()

@router.post("/recipes", response_model=RecipeResponse)
def create_recipe(recipe: RecipeCreate):
    new_recipe = {
        "id": len(recipes_db) + 1,
        "title": recipe.title,
        "description": recipe.description,
        "ingredients": recipe.ingredients,
        "owner_id": 1
    }
    recipes_db.append(new_recipe)
    return new_recipe

@router.get("/recipes", response_model=list[RecipeResponse])
def get_recipes():
    return recipes_db
