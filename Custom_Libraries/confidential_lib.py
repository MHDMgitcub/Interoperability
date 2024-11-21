import re

# Define the list of confidential words
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