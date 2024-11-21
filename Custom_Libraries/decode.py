import sys
from confidential_lib import decode_content

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python decode.py <file_path>")
        sys.exit(1)

    input_file_path = sys.argv[1]

    try:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            encoded_content = file.read()

        decoded_content = decode_content(encoded_content)
        print("Decoded Content:\n", decoded_content)

    except FileNotFoundError:
        print(f"Error: File not found: {input_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")