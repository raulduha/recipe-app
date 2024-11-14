from databases import Database
import sqlalchemy
from sqlalchemy import create_engine, MetaData

DATABASE_URL = "postgresql+asyncpg://admin:admin1@localhost/recipe_app"


database = Database(DATABASE_URL)
metadata = MetaData()

engine = create_engine(DATABASE_URL)
