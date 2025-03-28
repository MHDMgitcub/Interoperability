import sqlite3

# Path to database
db_path = '/storage/emulated/0/MHDM_git/database/recipes.db'


def get_recipe_data():
    """Fetches recipe data from SQLite"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM recipes")  # Adjust if needed
    recipe_data = cursor.fetchall()
    conn.close()
    return recipe_data