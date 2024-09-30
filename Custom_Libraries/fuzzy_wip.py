import sqlite3
import os
import sys

# Link to your repo
dir = '/storage/emulated/0/MHDM_git'
custom_libs = os.path.join(dir, 'Custom_Libraries')
sys.path.append(custom_libs)

# Import your own modules
import SQL_utilities
import utilities

def data_category(word, column):
    # Ensure database directory exists
    db_directory = "database"
    db_path = os.path.join(dir, db_directory, "recipes.db")

    # Step 1: Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Step 2: Register the custom function
    conn.create_function("DAMERAU_LEVENSHTEIN", 2, utilities.damerau_levenshtein)

    # Query to find categories where Damerau-Levenshtein distance is less than the threshold and column is not NULL
    query = f'''
        SELECT {column}, DAMERAU_LEVENSHTEIN({column}, ?) AS distance
        FROM recipes
        WHERE {column} IS NOT NULL
        ORDER BY distance ASC
        LIMIT 1;
    '''
    cursor.execute(query, (word,))

    # Fetch the closest match
    best_match = cursor.fetchone()
    threshold = 3

    # Step 3: Provide feedback
    if best_match and best_match[1] < threshold:
        data = best_match[0]
        print(f"Best match found: {data} (Distance: {best_match[1]})")
        return data
    else:
        cursor.execute(f'''
        SELECT DISTINCT {column} FROM recipes
        WHERE {column} IS NOT NULL;
        ''')

        # Step 4: Flatten the list of tuples into a list of strings
        categories = [category for (category,) in cursor.fetchall()]

        if categories:
            formatted_text = f"No match found...Available {column}s:\n"
            for category in categories:  # Directly use flattened list
                formatted_text += f"~~ {category} ~~\n"
            print(formatted_text)

        print(f'Do you want to create a new {column}? Otherwise, pick one of the existing ones.')
        user_input = input(f'{column}: ')

        # Step 5: Check Damerau-Levenshtein distance for the user's input
        closest_match = None
        min_distance = float('inf')

        for category in categories:
            distance = utilities.damerau_levenshtein(category, user_input)
            if distance < min_distance:
                min_distance = distance
                closest_match = category

        threshold = 2  # Define how close the match needs to be

        if min_distance <= threshold:
            print(f"Closest match found: {closest_match} (Distance: {min_distance})")
            data = closest_match
        else:
            print(f"No close match found. Creating new {column}: {user_input}")
            data = user_input

        # Step 6: Commit and close the connection
        conn.commit()
        conn.close()

        return data
