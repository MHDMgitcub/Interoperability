import os
import sqlite3

# Define the path for the database file
db_directory = "database"
db_path = os.path.join(db_directory, "recipes.db")
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Execute a query
cursor.execute('SELECT * FROM recipes')

# Fetch and print results
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close cursor and connection
cursor.close()
conn.close()

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