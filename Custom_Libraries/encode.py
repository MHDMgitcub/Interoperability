import os
import re

# List of confidential words to encode
CONFIDENTIAL_WORDS = ["MHDM_git", "password", "confidential", "private"]

def calculate_replacement(word):
    """Calculate the encoded replacement for a word."""
    first_letter = word[0]
    ascii_sum = sum(ord(char) for char in word)
    return f"{first_letter}{ascii_sum}"

def encode_content(content):
    """Encode confidential words in the given content."""
    for word in CONFIDENTIAL_WORDS:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        replacement = calculate_replacement(word)
        content = pattern.sub(replacement, content)
    return content

def decode_content(content):
    """Decode the encoded words back to their original confidential words."""
    replacement_map = {calculate_replacement(word): word for word in CONFIDENTIAL_WORDS}
    encoded_pattern = re.compile(r'([a-zA-Z])(\d+)')

    def replacement_match(match):
        first_letter = match.group(1)
        ascii_sum = int(match.group(2))
        encoded_str = f"{first_letter}{ascii_sum}"
        return replacement_map.get(encoded_str, match.group(0))

    return encoded_pattern.sub(replacement_match, content)

def find_and_encode_file(file_name):
    """Find the specified file in the folder and subfolders, read it, and print the encoded content."""
    folder_path = '/storage/emulated/0/MHDM_git/'
    file_name = file_name +".py"
    for root, _, files in os.walk(folder_path):
        if file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                print(f"Found and encoded content of '{file_path}':\n")
                encoded_content = encode_content(content)
                print(encoded_content)
                return
            except Exception as e:
                print(f"Error reading the file '{file_path}': {e}")
                return
    print(f"File '{file_name}' not found in the specified folder.")

def process_input(input_text):
    """Decide whether to treat the input as a filename or decode the content based on the input format."""
    if len(input_text.split()) == 1:
        # Single word input, treat as a filename
        find_and_encode_file(input_text)
    else:
        # Multiple words, treat as text for decoding
        try:
            decoded_content = decode_content(input_text)
            print("\nDecoded Content:")
            print(decoded_content)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_text = input()
    process_input(input_text)