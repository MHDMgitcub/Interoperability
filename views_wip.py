#cheapest
#in_season
#low_cal
#fastest
#deadline
#holiday
#from shop

import sqlite3
import os

# Step 1: Connect to the database
dir = '/storage/emulated/0/MHDM_git'
db_directory = "database"
db_path = os.path.join(dir, db_directory, "recipes.db")

connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Step 2: Define the SQL for the view
create_view_sql = """
CREATE VIEW recipes_with_total_quantity AS
SELECT 
    r.id AS recipe_id,
    r.name AS recipe_name,
    r.type AS recipe_type,
    r.creation_date,
    r.importance,
    IFNULL(SUM(rb.quantity), 0) AS total_quantity
FROM 
    recipes r
LEFT JOIN 
    recipe_breakdown rb ON r.id = rb.recipe_id
GROUP BY 
    r.id;
"""

# Step 3: Execute the SQL to create the view
cursor.execute(create_view_sql)
connection.commit()

# Step 4 (Optional): Verify the view by querying it
cursor.execute("SELECT * FROM recipes_with_total_quantity;")
rows = cursor.fetchall()

# Print the result
for row in rows:
    print(row)

# Step 5: Close the connection
connection.close()