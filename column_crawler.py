import os
import sqlite3
from  utilities import *
from AI_class_simple import calorie_processor

#Create rule
#    caps
#single record table for clarity
#final check

# Define the path for the database file
db_directory = "database"
db_path = os.path.join(db_directory, "recipes.db")

import os
import sqlite3

# Define the path for the database file
db_path = os.path.join("database", "recipes.db")

# Connect to SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# script to iterate though columns, and modify value:
    #arguments:
    #table name
    #column name
    #empty/full/complete to select what to show

def column_crawler(table_name, column_name, focus, rule=None):

    focus_dictionary = {
        'empty': f'WHERE {column_name} IS NULL',
        'full': f'WHERE {column_name} IS NOT NULL',
        'complete': ''
    }
    
    focus_clause = focus_dictionary.get(focus, '')
    
    cursor.execute(f"SELECT * FROM {table_name} {focus_clause}")
    records = cursor.fetchall()
  
    
    for record in records:
        input_value = input(f'{record}: ')
        
        
        
        if rule:
            new_value = rule(input_value)
        else:
            new_value = input_value
        
        if new_value:
            cursor.execute(
                f'UPDATE {table_name} SET {column_name} = ? '
                'WHERE id = ?',
                (new_value, record[0])
            )
            
    conn.commit()

        
def auto_column_crawler(table_name, column_name, focus, rule):
    # Dictionary for focus conditions
    focus_dictionary = {
        'empty': f'WHERE {column_name} IS NULL',
        'full': f'WHERE {column_name} IS NOT NULL',
        'complete': ''
    }
    
    # Get the focus condition or default to an empty string
    focus = focus_dictionary.get(focus, '')

    # Fetch records based on focus condition
    cursor.execute(f"SELECT id, {column_name} FROM {table_name} {focus}")
    records = cursor.fetchall()

    # Iterate over the fetched records and update the column
    for crawler in records:
        record_id = crawler[0]
        column_value = crawler[1]
        
        # Apply the rule to the column value
        print(crawler)
        new_value = rule(column_value)
        print(new_value)
        
        # Update the column with the new value
        cursor.execute(
            f"UPDATE {table_name} SET {column_name} = ? WHERE id = ?",
            (new_value, record_id)
        )
    
    # Commit the changes to the database
    conn.commit()

#column_crawler('ingredients', 'buy_where', 'empty')

#rule = lowercase
#column_crawler('recipes', 'importance', 'complete', rule)


#rule = lowercase
#column_crawler('recipes', 'type', 'empty', rule)

#rule = sentencecase
# Apply the rule using the function
#auto_column_crawler('ingredients', 'name', 'full', rule)


ingredient = 'Cucumber'
calorie_result, deviation = calorie_processor(ingredient)
cursor.execute(
    f"UPDATE ingredients SET calories_100  = ?, error_margin = ? WHERE name = ?",
    (calorie_result, deviation, ingredient)
)

    # Commit the changes to the database
conn.commit()

   

    