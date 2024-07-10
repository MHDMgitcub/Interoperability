import os
import sqlite3

# Define the path for the database file
db_directory = "database"
db_path = os.path.join(db_directory, "recipes.db")

# Connect to the SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Query to fetch all recipes
cursor.execute('SELECT id, name, ingredients, instructions FROM recipes')
recipes = cursor.fetchall()

# Print the fetched recipes
for recipe in recipes:
    print(f"ID: {recipe[0]}")
    print(f"Name: {recipe[1]}")
    print(f"Ingredients: {recipe[2]}")
    print(f"Instructions: {recipe[3]}")
    print("-" * 40)

# Close the connection
conn.close()

'''
read database
add new recipe
add new ingredients
check the season of each ingredient with groom
see if the recipe is in season
change
'''