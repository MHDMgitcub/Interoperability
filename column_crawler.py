import os
import sqlite3

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

def column_crawler(table_name, column_name, focus):
    
    rule_dictionary = {
    'empty': f'WHERE {column_name} IS NULL',
    'full': f'WHERE {column_name} IS NOT NULL',
    'complete': ''
    }
    
    rule = rule_dictionary.get(focus, '')

    cursor.execute(f"SELECT * FROM {table_name} {rule}")
    records = cursor.fetchall()
    
    
    
    # Iterate over the fetched records
    for crawler in records:
        new_value = input(f'{crawler}: ')
        if new_value:
            cursor.execute(
                f'UPDATE {table_name} SET {column_name} = ? '
                'WHERE id = ?',
                (new_value, crawler[0])
             )
            
        else:
            continue
        conn.commit()
        
column_crawler('recipes','type')

    
    
    