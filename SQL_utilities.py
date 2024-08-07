import os
import sqlite3
from tabulate import tabulate


#FUNCTION  to streamline the creation of a nicely formatted table
def format_table(table, style = 'pretty'):
    table_data = cursor.fetchall()
    headers = [description[0] for description in cursor.description]
    formatted_table = tabulate(table_data, headers, tablefmt=style)
    print(f"\n{table}")
    print(formatted_table)

# Define the path for the database file
db_directory = "database"
db_path = os.path.join(db_directory, "recipes.db")

# Connect to SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

recipe_name = 'Salade Estivale'
cursor.execute('''
    SELECT ingredients.name, ingredients.buy_where
    FROM ingredients
    JOIN recipe_breakdown ON ingredients.id = recipe_breakdown.ingredient_id
    JOIN recipes ON recipes.id = recipe_breakdown.recipe_id
    WHERE recipes.name = ?
''', (recipe_name,))

print(f'ingredient list for {recipe_name}:')
format_table(f'{recipe_name}')