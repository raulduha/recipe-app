from databases import Database
import sqlalchemy
from sqlalchemy import create_engine, MetaData

DATABASE_URL = "postgresql+asyncpg://postgres:your_password@localhost/recipe_app"

database = Database(DATABASE_URL)
metadata = MetaData()

engine = create_engine(DATABASE_URL)
