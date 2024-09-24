import os
import sqlite3
import sys
from datetime import date

#link to my repo
dir = '/storage/emulated/0/MHDM_git'
custom_libs = os.path.join(dir, 'Custom_Libraries')
sys.path.append(custom_libs)

#my own modules
import SQL_utilities
import utilities
import fuzzy_wip

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
        type = input('type: ')     
        # If no input is given, set `type` to None (which corresponds to NULL in SQL)
        if not type:
            print('...no type for now')
            type = None
        else:
            type = fuzzy_wip.data_category(type, 'type')      
            print(type)  
            
        importance = input('importance: ')   
        if not importance:
            print('...no importance for now')
            importance = None
        else:
            importance = fuzzy_wip.data_category(importance, 'importance')      
            print(importance)  
             
    
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
                    VALUES (?)''', (utilities.sentencecase(ingredient),))
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
    #conn.commit()

conn.close()



'''
def create recipe
    Add the shop where you buy the ingredient 
    AI timecount record
    AI season
    Image Parser
    shopping destination dictionnary
hierachy of shopping options
seasons
AI_column_crawler
sql utilities 
    add missing ingredient
types
origin of recipe
delete recipe and associated breakdown
alternative ingredient options
time counter
waste 

'''    