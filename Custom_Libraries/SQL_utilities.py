import os
import sqlite3
from tabulate import tabulate


#FUNCTION  to streamline the creation of a nicely formatted table
def format_table(cursor, table, style = 'pretty'):
    table_data = cursor.fetchall()
    headers = [description[0] for description in cursor.description]
    formatted_table = tabulate(table_data, headers, tablefmt=style)
    print(f"\n{table}")
    return formatted_table
    
# Define the path for the database file
#db_directory = "database"
#db_path = os.path.join(db_directory, "recipes.db")

# Connect to SQLite database
#conn = sqlite3.connect(db_path)
#cursor = conn.cursor()

def lookat_recipe(cursor, recipe_name, ):
    cursor.execute('''
        SELECT ingredients.name, ingredients.buy_where
        FROM ingredients
        JOIN recipe_breakdown ON ingredients.id = recipe_breakdown.ingredient_id
        JOIN recipes ON recipes.id = recipe_breakdown.recipe_id
        WHERE recipes.name = ?
    ''', (recipe_name,))
    print(f'ingredient list for {recipe_name}:')
    return format_table(cursor, recipe_name)
    
def random_recipe(cursor):
    cursor.execute('''
        SELECT recipes.name AS recipe_name, ingredients.name AS ingredient_name, ingredients.buy_where
        FROM ingredients
        JOIN recipe_breakdown ON ingredients.id = recipe_breakdown.ingredient_id
        JOIN recipes ON recipes.id = recipe_breakdown.recipe_id
        WHERE recipes.id = (
            SELECT id
            FROM recipes
            ORDER BY RANDOM()
            LIMIT 1
        )
    ''')

    table_data = cursor.fetchall()
    
    if table_data:
        recipe_name = table_data[0][0]
        formatted_text = f"{recipe_name}...\n"
        
        for index, (recipe_name, ingredient, shop) in enumerate(table_data, start=1):
            shop_info = shop if shop else ""
            formatted_text += f"~ {index:2}. {ingredient} ~ {shop_info}\n"
    
    return formatted_text



