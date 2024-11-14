# test_db_psycopg2.py
import psycopg2
from psycopg2 import OperationalError

def test_connection():
    try:
        # Replace with your actual database connection details
        connection = psycopg2.connect(
            dbname="recipe_app",
            user="admin",
            password="admin1",
            host="localhost",
            port="5432"
        )
        print("Database connection successful!")
        connection.close()
    except OperationalError as e:
        print(f"Error connecting to database: {e}")

if __name__ == "__main__":
    test_connection()