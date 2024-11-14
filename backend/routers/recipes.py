from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas import RecipeCreate, RecipeResponse
from models import Recipe, RecipeIngredient, Ingredient, UnitOfMeasurement, Quantity # Import the Recipe model from models.py
from database import get_db  # Import the dependency to get a DB session

router = APIRouter()

@router.post("/recipes", response_model=RecipeResponse)
def create_recipe(recipe: RecipeCreate, db: Session = Depends(get_db)):
    # Create a new recipe in the database
    new_recipe = Recipe(
        title=recipe.title,
        description=recipe.description,
        owner_id=recipe.owner_id  # You should later replace with the logged-in user's ID
    )
    
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)  # Get the ID of the new recipe
    
    # Now, process the ingredients and add them to the recipe_ingredients table
    for ingredient_detail in recipe.ingredients:
        # Retrieve the ingredient, unit, and quantity from the database
        ingredient = db.query(Ingredient).filter(Ingredient.id == ingredient_detail.ingredient_id).first()
        unit = db.query(UnitOfMeasurement).filter(UnitOfMeasurement.id == ingredient_detail.unit_id).first()
        quantity = db.query(Quantity).filter(Quantity.id == ingredient_detail.quantity_id).first()
        
        if not ingredient or not unit or not quantity:
            raise HTTPException(
                status_code=400,
                detail="Invalid ingredient, unit, or quantity ID"
            )
        
        # Add the RecipeIngredient relationship to the database
        recipe_ingredient = RecipeIngredient(
            recipe_id=new_recipe.id,
            ingredient_id=ingredient.id,
            unit_id=unit.id,
            quantity_id=quantity.id
        )
        db.add(recipe_ingredient)

    # Commit the transaction to save the recipe and recipe_ingredients
    db.commit()

    # Return the created recipe
    return new_recipe

@router.get("/recipes", response_model=list[RecipeResponse])
def get_recipes(db: Session = Depends(get_db)):
    # Retrieve all recipes from the database
    recipes = db.query(Recipe).all()
    return recipes
