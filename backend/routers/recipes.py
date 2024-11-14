from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas import RecipeCreate, RecipeResponse
from models import Recipe  # Import the Recipe model from models.py
from database import get_db  # Import the dependency to get a DB session

router = APIRouter()

@router.post("/recipes", response_model=RecipeResponse)
def create_recipe(recipe: RecipeCreate, db: Session = Depends(get_db)):
    # Create a new recipe in the database
    new_recipe = Recipe(
        title=recipe.title,
        description=recipe.description,
        ingredients=recipe.ingredients,
        owner_id=1  # You should later replace '1' with the logged-in user's ID
    )
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)  # Refresh to get the ID of the new recipe
    return new_recipe

@router.get("/recipes", response_model=list[RecipeResponse])
def get_recipes(db: Session = Depends(get_db)):
    # Retrieve all recipes from the database
    recipes = db.query(Recipe).all()
    return recipes
