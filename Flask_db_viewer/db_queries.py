import sqlite3

DB_PATH = '/storage/emulated/0/MHDM_git/database/recipes.db'

def get_db_connection():
    """Creates a database connection with thread safety enabled."""
    return sqlite3.connect(DB_PATH, check_same_thread=False)
    
def get_all_recipes():
    """Fetch all recipes as a list of dictionaries."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM recipes")

    columns = [desc[0] for desc in cursor.description]  # Get column names
    rows = cursor.fetchall()

    conn.close()

    # Convert list of tuples into list of dictionaries
    recipes = [dict(zip(columns, row)) for row in rows]

    return recipes
    
def get_recipe_details_by_id(recipe_id):
    """Fetch a recipe's details by ID."""
    conn = get_db_connection()
    cursor = conn.cursor()

    query = '''
        SELECT recipes.id, recipes.name AS recipe_name, ingredients.name AS ingredient_name, ingredients.buy_where
        FROM recipes
        JOIN recipe_breakdown ON recipes.id = recipe_breakdown.recipe_id
        JOIN ingredients ON ingredients.id = recipe_breakdown.ingredient_id
        WHERE recipes.id = ?
    '''
    cursor.execute(query, (recipe_id,))
    results = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]  # Get column names dynamically
    conn.close()

    if results:
        # Convert results into list of dictionaries
        recipes_list = [dict(zip(columns, row)) for row in results]

        # Extract the recipe ID, name, and ingredients correctly
        recipe_id = recipes_list[0]["id"]  
        recipe_name = recipes_list[0]["recipe_name"]  # Now correctly mapped
        ingredients = [(row["ingredient_name"], row["buy_where"]) for row in recipes_list]

        return {"id": recipe_id, "name": recipe_name, "ingredients": ingredients}

    return None  # Return None if no results found