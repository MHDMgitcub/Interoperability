import os
import sqlite3

# Define the path for the database file
db_directory = "database"
db_path = os.path.join(db_directory, "recipes.db")

try:
    # Connect to SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    alias = 'Avocado'

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
            # Delete all records with similar names except for the one with the earliest id
            cursor.execute('''
                DELETE FROM ingredients
                WHERE name LIKE ? AND id != ?
            ''', (f'%{alias}%', earliest_id))

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
            print("No records found with the given alias.")

except sqlite3.Error as e:
    print(f"An error occurred: {e}")
    if conn:
        conn.rollback()

finally:
    # Ensure the connection is always closed
    if conn:
        conn.close()
