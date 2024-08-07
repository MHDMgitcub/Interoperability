import os
import sqlite3
from datetime import date
from utilities import *    

# Define the path for the database file
db_directory = "database"
db_path = os.path.join(db_directory, "recipes.db")

# Connect to SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

pending_change = False

# CREATE - input all recipe info
while True:
    recipe = input('Recipe name: ').strip().lower()
    today = date.today()

    # Recover recipe_id with case- and whitespace-insensitive search
    cursor.execute('''
        SELECT id
        FROM recipes
        WHERE LOWER(TRIM(name)) = ?
    ''', (recipe,))
    recipe_data = cursor.fetchone()

    if recipe_data:
        print('Recipe already exists')
    elif recipe:
        print('A new recipe is being created')
        
        # Insert the new recipe info
        cursor.execute('''
            INSERT INTO recipes (name, creation_date)
            VALUES (?, ?)''', (titlecase(recipe), today))
        pending_change = True
        
        # Retrieve the newly inserted recipe's ID
        recipe_id = cursor.lastrowid
        print(f'New recipe created with ID: {recipe_id}')
        
        # CREATE - Input all ingredients info        
        while True:
            ingredient = input('Ingredient: ').strip().lower()

            if not ingredient:
                break  # Exit the loop if no input

            # Recover ingredient_id with case- and whitespace-insensitive search
            cursor.execute('''
                SELECT id
                FROM ingredients
                WHERE LOWER(TRIM(name)) = ?
            ''', (ingredient,))
            ingredient_data = cursor.fetchone()

            if ingredient_data:
                print('Ingredient already exists...')
                ingredient_id = ingredient_data[0]
            else:
                print('A new ingredient is being created...')
                cursor.execute('''
                    INSERT INTO ingredients (name)
                    VALUES (?)''', (sentencecase(ingredient),))
                pending_change = True
                
                # Retrieve the newly inserted ingredient's ID
                ingredient_id = cursor.lastrowid

            # Interconnect recipe with ingredients through the breakdown table
            print(f'Ingredient with ID: {ingredient_id}')               
            cursor.execute('''
                INSERT INTO recipe_breakdown (ingredient_id, recipe_id)
                VALUES (?, ?)''', (ingredient_id, recipe_id))
            pending_change = True

    else:
        print('No recipe name provided.')
        break

if pending_change:
    print('Changes written to database...')
    conn.commit()

conn.close()
