import base64
import re

# Secret list of words to encrypt/decrypt
SECRET_WORDS = ["confidential", "secret", "password"]

def encryption_method(word):
    """Custom encryption logic (base64 encoding as default)."""
    return base64.urlsafe_b64encode(word.encode()).decode()

def decryption_method(word):
    """Custom decryption logic (base64 decoding)."""
    return base64.urlsafe_b64decode(word.encode()).decode()

def encrypt_text(text):
    """Encrypt specific words in the text using the secret list."""
    for word in SECRET_WORDS:
        encrypted_word = encryption_method(word)
        # Use regular expression to handle case-insensitive replacement
        text = re.sub(rf'\b{re.escape(word)}\b', encrypted_word, text, flags=re.IGNORECASE)
    return text

def decrypt_text(text):
    """Decrypt specific words in the text using the secret list."""
    for word in SECRET_WORDS:
        encrypted_word = encryption_method(word)
        # Use regular expression to handle case-insensitive replacement
        text = re.sub(rf'\b{re.escape(encrypted_word)}\b', word, text, flags=re.IGNORECASE)
    return text

def auto_process_text(text):
    """
    Automatically determine whether to encrypt or decrypt the text.
    If any encrypted word from the SECRET_WORDS list appears in the text, decrypt all.
    If no encrypted words are found, encrypt all words in the SECRET_WORDS list.
    """
    # Check if any encrypted word is in the text
    for word in SECRET_WORDS:
        encrypted_word = encryption_method(word)
        if encrypted_word in text:
            return decrypt_text(text)  # Decrypt all words if any encrypted word is found

    return encrypt_text(text)  # Encrypt all words if no encrypted word is found

def main():
    print("Paste your text below (line breaks will be preserved). Press Enter twice to finish:")
    lines = []
    while True:
        try:
            line = input()
            if line == "" and (len(lines) > 0 and lines[-1] == ""):
                break
            lines.append(line)
        except EOFError:  # Handle unexpected EOF for non-interactive environments
            break

    # Combine all input lines, preserving all line breaks
    text = "\n".join(lines)

    # Process text (auto-detect encryption or decryption)
    processed_text = auto_process_text(text)

    print("\nProcessed Text (line breaks preserved):")
    print(processed_text)

if __name__ == "__main__":
    main()