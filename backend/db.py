from databases import Database
import sqlalchemy
from sqlalchemy import create_engine, MetaData

DATABASE_URL = "postgresql+asyncpg://your_username:your_password@localhost/CookingRecipes"

database = Database(DATABASE_URL)
metadata = MetaData()

engine = create_engine(DATABASE_URL)
