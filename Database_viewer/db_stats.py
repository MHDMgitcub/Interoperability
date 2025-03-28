import sqlite3
import os

#view: recipes_with_total_quantity

def extract_sqlite_schema(db_path):
    # Connect to the SQLite database
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Fetch all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    schema_details = []

    for table in tables:
        table_name = table[0]
        schema_details.append(f"Table: {table_name}")

        # Fetch column details for each table
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()

        for column in columns:
            column_id, name, data_type, not_null, default_value, pk = column
            schema_details.append(
                f"  Column: {name}, Type: {data_type}, Not Null: {bool(not_null)}, "
                f"Default: {default_value}, Primary Key: {bool(pk)}"
            )
        schema_details.append("")  # Add a blank line between tables for readability

    # Close the connection
    connection.close()

    return "\n".join(schema_details)
    
def list_views(database_path):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # Query to fetch all views from the sqlite_master table
        cursor.execute("SELECT name, sql FROM sqlite_master WHERE type = 'view';")
        views = cursor.fetchall()

        if views:
            print("Views in the database:")
            for view in views:
                print(f"\nView Name: {view[0]}")
                print(f"SQL Definition: {view[1]}")
        else:
            print("No views found in the database.")

        # Close the connection
        cursor.close()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error accessing database: {e}")

# Replace 'your_database.db' with the path to your SQLite database file
list_views("your_database.db")

# Example usage
if __name__ == "__main__":
    dir = '/storage/emulated/0/MHDM_git'
    db_directory = "database"
    db_path = os.path.join(dir, db_directory, "recipes.db")

    schema_text = extract_sqlite_schema(db_path)
    print(schema_text)
    
    list_views(db_path)