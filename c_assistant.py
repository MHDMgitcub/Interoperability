import os
import sqlite3
from season_converter import str_season

# Define the path for the database file
db_directory = "database"
db_path = os.path.join(db_directory, "recipes.db")

# Connect to SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# CREATE - input all ingredients info
while True:
    ingredient = input('Ingredient: ')
    if not ingredient:
        break  # Exit the script if an empty value is entered
                 
#recover recipe_id   
cursor.execute('''       
    SELECT *
    FROM ingredients
    WHERE name = ?
    ''', (ingredient,))
ingredient_data = cursor.fetchall()

if ingredient_data:
    quantity = input('Quantity: ')
    
    cursor.execute('''
        SELECT id FROM ingredients
        WHERE name = ?
        ''', (ingredient,))    
    ingredient_id = cursor.fetchone()[0]
           
    cursor.executemany('''
        INSERT INTO recipe_breakdown (recipe_id, ingredient_id, quantity)
        VALUES (?, ?, ?)
                    ''',[(recipe_id, ingredient_id, quantity)])
             
           
else:
    quantity = input('Quantity: ')
    packing = input('Packing: ')
    price = input('Price: ')
    season 
        
    cursor.executemany('''
        INSERT INTO ingredients (name, packing)
        VALUES (?, ?)''', [(ingredient, packing)])    
             
    cursor.execute('''
        SELECT id FROM ingredients
        WHERE name = ?
            ''', (ingredient,))
    ingredient_id = cursor.fetchone()[0]    
       
    cursor.executemany('''
        INSERT INTO recipe_breakdown (recipe_id, ingredient_id, quantity)
        VALUES (?, ?, ?)
            ''',[(recipe_id, ingredient_id, quantity)])

'''
def create ingredient
    AI checker
def create recipe
    AI checker
    Image Parser
'''    


'''
add new recipe
add new ingredients
check the season of each ingredient with groom
see if the recipe is in season
'''