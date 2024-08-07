import pdb

import os
import sqlite3
from datetime import date
from utilities import *
#from season_converter import str_season    

# Define the path for the database file
db_directory = "database"
db_path = os.path.join(db_directory, "recipes.db")

# Connect to SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
pending_change = False #track changes prior to commit
flag = True
# CREATE - input all recipe info
while flag == True:
    recipe = input('recipe name: ').strip().lower()
    today = date.today()
    

    # Recover recipe_id with case- and whitespace-insensitive search
    cursor.execute('''
        SELECT *
        FROM recipes
        WHERE LOWER(TRIM(name)) = ?
    ''', (recipe,))
    recipe_data = cursor.fetchall()
    
    if recipe_data:
        print('Recipe already exists')
                        
    elif recipe:
        print ('A new recipe is being created')
                     
        # Insert the new recipe info
        cursor.executemany('''
            INSERT INTO recipes (name, creation_date)
            VALUES (?, ?)''', [(titlecase(recipe), today)])  
            
        pending_change = True
    
        # Retrieve the newly inserted recipe's ID
        cursor.execute('''
            SELECT id FROM recipes
            WHERE LOWER(TRIM(name)) = ?
        ''', (recipe,))
        recipe_id = cursor.fetchone()[0]
    
        print(f'New recipe created with ID: {recipe_id}') 
            
        # CREATE - Once  recipe created, input all ingredients info        
        # while loop continuously runs until whitespace breaks out 
        while True:      
            ingredient = input('Ingredient: ').strip().lower()
        
            # Recover ingredient_id with case- and whitespace-insensitive search
            cursor.execute('''
                SELECT *
                FROM ingredients
                WHERE LOWER(TRIM(name)) = ?
            ''', (ingredient,))
            ingredient_data = cursor.fetchall()
        
            if ingredient_data:
                print('Ingredient already exists...')
                #script continues to retrieve the ingredient ID              
                                
            if ingredient:
                print ('A new ingredient is being created...')
                
               # Insert the new ingredient info
                cursor.execute('''
                    INSERT INTO ingredients (name)
                    VALUES (?)''', (sentencecase(ingredient),))  
                
                pending_change = True
            else:
                if pending_change:
                    print('Changes written to database...')
                    #conn.commit()
                    pending_change = False
                else:
                    print('no changes')
                flag = False
                break
        
                # Retrieve the newly inserted ingredient's ID
            cursor.execute('''
                SELECT id FROM ingredients
                WHERE LOWER(TRIM(name)) = ?
             ''', (ingredient,))
            ingredient_id = cursor.fetchone()[0]
        
            #interconnect recipe with ingredients through the breakdown table
            print(f'Ingredient with ID: {ingredient_id}')               
            cursor.executemany('''
                INSERT INTO recipe_breakdown (ingredient_id, recipe_id)
                VALUES (?,?)''', [(ingredient_id, recipe_id)])
                    
            pending_change = True
 
    else:
          flag = False
          

'''
def create ingredient
    AI checker
def create recipe
    AI checker
    Image Parser
seasons
calories
AI_column_crawler
types
origin of recipe
delete recipe and associates breakdown
alternative ingredient options

'''    


'''
check the season of each ingredient with groom
see if the recipe is in season
'''