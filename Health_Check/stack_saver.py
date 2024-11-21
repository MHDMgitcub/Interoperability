


import os

# Get the folder path where this script is located
folder_path = os.path.dirname(__file__)

# Get the name of this script
script_name = os.path.basename(__file__)

# Define the file extensions you want to look for, in the desired order
file_extensions = ['.html', '.css', '.js', '.json']  # Adjust this list as needed

try:
    files = []
    
    # Group files by the order of extensions in file_extensions
    for ext in file_extensions:
        matching_files = sorted(
            f for f in os.listdir(folder_path)
            if os.path.isfile(os.path.join(folder_path, f))
            and f != script_name
            and f.endswith(ext)
        )
        files.extend(matching_files)

    # Print each matching file name and its content in the specified order
    for file in files:
        print(f"Filename: {file}")
        
        # Read and print the content of the file
        with open(os.path.join(folder_path, file), 'r') as f:
            content = f.read()
            print(f"\nContent:\n{content}\n\n")  # Print the content of the file

except FileNotFoundError:
    print(f"The folder path '{folder_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")