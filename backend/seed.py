from sqlalchemy.orm import Session
from database import engine, SessionLocal
from models import Ingredient, UnitOfMeasurement, Quantity

# Crear la sesión de base de datos
db = SessionLocal()

def seed_ingredients(db: Session):
    ingredients = [
        Ingredient(name="Tomato"),
        Ingredient(name="Onion"),
        Ingredient(name="Garlic"),
        Ingredient(name="Chicken"),
        Ingredient(name="Beef")
    ]
    db.add_all(ingredients)
    db.commit()
    print("Ingredients seeded successfully.")

def seed_units(db: Session):
    units = [
        UnitOfMeasurement(unit="kg"),
        UnitOfMeasurement(unit="g"),
        UnitOfMeasurement(unit="L"),
        UnitOfMeasurement(unit="ml"),
        UnitOfMeasurement(unit="tsp"),
        UnitOfMeasurement(unit="tbsp"),
    ]
    db.add_all(units)
    db.commit()
    print("Units seeded successfully.")

def seed_quantities(db: Session):
    quantities = [
        Quantity(quantity=1),
        Quantity(quantity=2),
        Quantity(quantity=0.5),
        Quantity(quantity=0.25),
        Quantity(quantity=3)
    ]
    db.add_all(quantities)
    db.commit()
    print("Quantities seeded successfully.")

def main():
    print("Seeding data...")
    seed_ingredients(db)
    seed_units(db)
    seed_quantities(db)
    db.close()

if __name__ == "__main__":
    main()
