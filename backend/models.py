from sqlalchemy import Column, Integer, String, Text, ForeignKey, TIMESTAMP, DECIMAL, Boolean, func
from sqlalchemy.orm import relationship
from database import Base  # Ensure Base is imported from your database.py file

# User model (your current version with minor modifications)
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True, nullable=True)
    password_hash = Column(String)
    role = Column(String, default="user")

    # Using SQLAlchemy's func.now() for timestamps
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())

    # Relationship with Recipe
    recipes = relationship("Recipe", back_populates="owner")

# Recipe model
class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())

    # Foreign key to User
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship("User", back_populates="recipes")

    # Relationships for many-to-many associations
    tags = relationship("RecipeTag", back_populates="recipe")
    ingredients = relationship("RecipeIngredient", back_populates="recipe")

# Ingredient model
class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    # Relationship with RecipeIngredient
    recipe_ingredients = relationship("RecipeIngredient", back_populates="ingredient")

# Unit of Measurement model
class UnitOfMeasurement(Base):
    __tablename__ = 'units_of_measurement'

    id = Column(Integer, primary_key=True, index=True)
    unit = Column(String, unique=True, nullable=False)

    # Relationship with RecipeIngredient
    recipe_ingredients = relationship("RecipeIngredient", back_populates="unit")

# Quantity model
class Quantity(Base):
    __tablename__ = 'quantities'

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(DECIMAL, nullable=False)

    # Relationship with RecipeIngredient
    recipe_ingredients = relationship("RecipeIngredient", back_populates="quantity")

# Tag model
class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    # Relationship with RecipeTag
    recipe_tags = relationship("RecipeTag", back_populates="tag")

# RecipeTag model for many-to-many relationship between Recipe and Tag
class RecipeTag(Base):
    __tablename__ = 'recipe_tags'

    recipe_id = Column(Integer, ForeignKey('recipes.id'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('tags.id'), primary_key=True)

    # Relationships
    recipe = relationship("Recipe", back_populates="tags")
    tag = relationship("Tag", back_populates="recipe_tags")

# RecipeIngredient model for many-to-many relationship between Recipe and Ingredient
class RecipeIngredient(Base):
    __tablename__ = 'recipe_ingredients'

    recipe_id = Column(Integer, ForeignKey('recipes.id'), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'), primary_key=True)
    unit_id = Column(Integer, ForeignKey('units_of_measurement.id'))
    quantity_id = Column(Integer, ForeignKey('quantities.id'))

    # Relationships
    recipe = relationship("Recipe", back_populates="ingredients")
    ingredient = relationship("Ingredient", back_populates="recipe_ingredients")
    unit = relationship("UnitOfMeasurement", back_populates="recipe_ingredients")
    quantity = relationship("Quantity", back_populates="recipe_ingredients")
