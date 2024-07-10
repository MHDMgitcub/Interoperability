import sqlite3
import os
from tabulate import tabulate

# Define the path for the database file
db_directory = "database"
db_file = "recipes.db"
db_path = os.path.join(db_directory, db_file)

# Connect to the database at the specified location or create it if it doesn't exist
connection = sqlite3.connect(db_path)
print(f"Database file '{db_file}' successfully connected @ path: \n '{db_path}'.")
cursor = connection.cursor()

#FUNCTION  to streamline the creation of a nicely formatted table
def format_table(table, style):
    table_data = cursor.fetchall()
    headers = [description[0] for description in cursor.description]
    formatted_table = tabulate(table_data, headers, tablefmt=style)
    print(f"\n{table}")
    print(formatted_table)

# Retrieve data from the recipes table
cursor.execute(
    '''
    SELECT *
    FROM recipes; 
    '''
)
format_table("recipes", "pretty")

# Retrieve data from the recipe_breakdown table
cursor.execute(
    '''
    SELECT *
    FROM recipe_breakdown; 
    '''
)
format_table("recipe_breakdown", "pretty")

# Retrieve data from the ingredients table
cursor.execute(
    '''
    SELECT *
    FROM ingredients; 
    '''
)
format_table("ingredients", "pretty")

# Close the cursor and the connection
cursor.close()
connection.close()

'''
#import results from other independently working scripts
import Query_price
Query_price.get_recipe_price()
Query_price.get_remaining_ingredients()
'''