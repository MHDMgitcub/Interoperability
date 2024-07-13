#works

import os
import sqlite3

# Define the path for the database file
db_directory = "database"
db_path = os.path.join(db_directory, "recipes.db")


# Connect to your SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create a new table with the same structure but without the 'creation_date' column
cursor.execute('''
CREATE TABLE recipes_new (
    id INTEGER PRIMARY KEY,
    name TEXT,
    type TEXT
);
''')

# Copy data from the old table to the new table
cursor.execute('''
INSERT INTO recipes_new (id, name, type)
SELECT id, name, type
FROM recipes;
''')

# Drop the old table
cursor.execute('DROP TABLE recipes;')

# Rename the new table to the original table's name
cursor.execute('ALTER TABLE recipes_new RENAME TO recipes;')

# Add the new column 'creation_date' with 'DATE' as the data type
cursor.execute('''
ALTER TABLE recipes
ADD COLUMN creation_date DATE;
''')

'''
remote bracelets to commit
# Commit changes and close connection
conn.commit()
conn.close()
'''