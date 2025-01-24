#improve - replace with levenstein distance


import os
import sqlite3

# Define the path for the database file
db_directory = "database"
db_path = os.path.join(db_directory, "recipes.db")

#Make sure the reconnection is made


def SQL_merge_similar(db_path, alias):
    try:
        # Connect to SQLite database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()           
    
        # Retrieve records matching the alias
        cursor.execute('''
            SELECT id, name FROM ingredients
            WHERE name LIKE ?
        ''', (f'%{alias}%',))
    
        results = cursor.fetchall()
        print("Current records with alias:", results)
    
        choice_1 = input('Do you want to merge? (y/n): ').strip().lower()
    
        if choice_1 == 'y':
            # Find the earliest id among the records with similar names
            cursor.execute('''
                SELECT MIN(id) FROM ingredients
                WHERE name LIKE ?
            ''', (f'%{alias}%',))
            
            earliest_id = cursor.fetchone()[0]
    
            if earliest_id is not None:
                # Record IDs of ingredients to be deleted
                cursor.execute('''
                    SELECT id FROM ingredients
                    WHERE name LIKE ? AND id != ?
                ''', (f'%{alias}%', earliest_id))
                ids_to_delete = [row[0] for row in cursor.fetchall()]
    
                if ids_to_delete:
                    # Update recipe_breakdown table to reassign references
                    cursor.execute(f'''
                        UPDATE recipe_breakdown
                        SET ingredient_id = ?
                        WHERE ingredient_id IN ({','.join('?' * len(ids_to_delete))})
                    ''', [earliest_id] + ids_to_delete)
    
                    # Delete duplicate ingredients
                    cursor.execute('''
                        DELETE FROM ingredients
                        WHERE id IN ({})
                    '''.format(','.join('?' * len(ids_to_delete))), ids_to_delete)
    
                    # Retrieve and print the remaining records
                    cursor.execute('''
                        SELECT id, name FROM ingredients
                        WHERE name LIKE ?
                    ''', (f'%{alias}%',))
                    results = cursor.fetchall()
                    print("Updated records with alias:", results)
    
                    if input('Happy with the result? (y/n): ').strip().lower() == 'y':
                        conn.commit()
                        print("Changes committed.")
                    else:
                        print("No changes were committed.")
                        conn.rollback()
                else:
                    print("No duplicates found to merge.")
            else:
                print("No records found with the given alias.")
    
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        if conn:
            conn.rollback()
    
    finally:
        # Ensure the connection is always closed
        if conn:
            conn.close()
            
alias = 'booya'
SQL_merge_similar(db_path, alias)

#'''    -   NEXT    -    '''


def add_columns_to_table(db_path, table_name, columns):
    """
    Adds specified columns to a given table in an SQLite database.
    
    Parameters:
        db_path (str): Path to the SQLite database.
        table_name (str): Name of the table to alter.
        columns (dict): A dictionary where the keys are column names and the values are their data types.
        
    Example:
        add_columns_to_table('your_database.db', 'ingredients', 
                             {'calories_100': 'REAL', 'error_margin': 'NUMERIC'})
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Add each column to the specified table
    for column_name, data_type in columns.items():
        cursor.execute(f"""
        ALTER TABLE {table_name} 
        ADD COLUMN {column_name} {data_type};
        """)
        print(f"Column '{column_name}' of type '{data_type}' added to table '{table_name}'.")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
#-     NEXT     -

def group_ingredients(db_path):
    try:
        # Connect to SQLite database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()           
    
        # Retrieve records matching the alias
        cursor.execute('''
            SELECT name FROM ingredients           
        ''', (f'%{alias}%',))
#        
#group_ingredients(db_path)
#    
#-   ENACT    -

#add_columns_to_table(db_path, 'ingredients', {'calories_100': 'REAL', 'error_margin': 'REAL'})