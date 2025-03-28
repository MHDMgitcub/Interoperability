from local_server_startup import run_server
import sqlite3

#link to my repo
db_path = '/storage/emulated/0/MHDM_git/database/recipes.db'

# Connect to SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Fetch data from the database
cursor.execute('SELECT * FROM recipes')
recipe_data = cursor.fetchall()

# great homemade web IDE
run_server()