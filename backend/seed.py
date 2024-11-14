from sqlalchemy.orm import Session
from models import Ingredient, UnitOfMeasurement, Quantity
from database import get_db
from contextlib import contextmanager

# Crear un contexto para la sesión de la base de datos
@contextmanager
def get_session():
    db = next(get_db())
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

def seed_ingredients(db: Session):
    ingredients = ["Tomato", "Onion", "Garlic", "Chicken", "Beef"]

    for ingredient_name in ingredients:
        # Verificar si el ingrediente ya existe antes de agregarlo
        existing_ingredient = db.query(Ingredient).filter(Ingredient.name == ingredient_name).first()
        if not existing_ingredient:
            new_ingredient = Ingredient(name=ingredient_name)
            db.add(new_ingredient)

def seed_units(db: Session):
    units = ["kg", "g", "l", "ml", "cup", "tbsp", "tsp"]

    for unit_name in units:
        existing_unit = db.query(UnitOfMeasurement).filter(UnitOfMeasurement.unit == unit_name).first()
        if not existing_unit:
            new_unit = UnitOfMeasurement(unit=unit_name)
            db.add(new_unit)

def seed_quantities(db: Session):
    quantities = [1, 2, 3, 4, 5]

    for quantity_value in quantities:
        existing_quantity = db.query(Quantity).filter(Quantity.quantity == quantity_value).first()
        if not existing_quantity:
            new_quantity = Quantity(quantity=quantity_value)
            db.add(new_quantity)

def main():
    print("Seeding data...")
    with get_session() as db:
        seed_ingredients(db)
        seed_units(db)
        seed_quantities(db)
    print("Seeding completed successfully!")

if __name__ == "__main__":
    main()
