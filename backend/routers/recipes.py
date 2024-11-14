from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session, joinedload
from schemas import IngredientDetail, RecipeCreate, RecipeResponse, IngredientResponse, UnitResponse, QuantityResponse
from models import Recipe, RecipeIngredient, Ingredient, UnitOfMeasurement, Quantity
from database import get_db
from models import Recipe, RecipeIngredient, Ingredient
router = APIRouter()

@router.post("/", response_model=RecipeResponse)
def create_recipe(recipe: RecipeCreate, db: Session = Depends(get_db)):
    # Crear la receta en la base de datos
    new_recipe = Recipe(
        title=recipe.title,
        description=recipe.description,
        owner_id=recipe.owner_id
    )
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)

    # Añadir los ingredientes a la receta
    for ingredient_detail in recipe.ingredients:
        ingredient = db.query(Ingredient).filter(Ingredient.id == ingredient_detail.ingredient_id).first()
        unit = db.query(UnitOfMeasurement).filter(UnitOfMeasurement.id == ingredient_detail.unit_id).first()
        quantity = db.query(Quantity).filter(Quantity.id == ingredient_detail.quantity_id).first()

        if not ingredient or not unit or not quantity:
            raise HTTPException(status_code=400, detail="Invalid ingredient, unit, or quantity ID")

        recipe_ingredient = RecipeIngredient(
            recipe_id=new_recipe.id,
            ingredient_id=ingredient.id,
            unit_id=unit.id,
            quantity_id=quantity.id
        )
        db.add(recipe_ingredient)

    db.commit()

    # Devolver la respuesta en el formato que espera Pydantic
    return RecipeResponse(
        id=new_recipe.id,
        title=new_recipe.title,
        description=new_recipe.description,
        owner_id=new_recipe.owner_id,
        ingredients=[
            {
                "ingredient_id": ing.ingredient_id,
                "unit_id": ing.unit_id,
                "quantity_id": ing.quantity_id,
                "name": ing.ingredient.name,
                "unit": ing.unit.unit,
                "quantity": ing.quantity.quantity
            }
            for ing in new_recipe.ingredients
        ]
    )

# Endpoint para obtener todas las recetas
@router.get("/", response_model=list[RecipeResponse])
def get_recipes(db: Session = Depends(get_db)):
    recipes = db.query(Recipe).options(
        joinedload(Recipe.ingredients).joinedload(RecipeIngredient.ingredient),
        joinedload(Recipe.ingredients).joinedload(RecipeIngredient.unit),
        joinedload(Recipe.ingredients).joinedload(RecipeIngredient.quantity)
    ).all()

    recipes_data = []
    for recipe in recipes:
        ingredients = [
            {
                "ingredient_id": ing.ingredient_id,
                "unit_id": ing.unit_id,
                "quantity_id": ing.quantity_id,
                "name": ing.ingredient.name,
                "unit": ing.unit.unit,
                "quantity": ing.quantity.quantity
            }
            for ing in recipe.ingredients
        ]
        recipes_data.append({
            "id": recipe.id,
            "title": recipe.title,
            "description": recipe.description,
            "owner_id": recipe.owner_id,
            "ingredients": ingredients
        })
    
    return recipes_data
@router.get("/ingredients", response_model=list[IngredientResponse])
def get_ingredients(db: Session = Depends(get_db)):
    return db.query(Ingredient).all()

@router.get("/units", response_model=list[UnitResponse])
def get_units(db: Session = Depends(get_db)):
    return db.query(UnitOfMeasurement).all()

@router.get("/quantities", response_model=list[QuantityResponse])
def get_quantities(db: Session = Depends(get_db)):
    return db.query(Quantity).all()
