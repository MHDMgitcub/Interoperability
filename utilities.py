
def sentencecase(s):
    if s:  # Check if the string is not empty
        return s[0].upper() + s[1:]
    return s  # Return the original string if it's empty

def lowercase(s):
    if s:  # Check if the string is not empty
        return s.lower()
    return s  # Return the original string if it's empty

    
def titlecase(s):
    # List of words to remain in lowercase
    exceptions = ['and', 'à', 'are', 'of', 'or', 'but', 'a', 'an', 'the', 'in', 'on', 'at', 'to', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'from', 'up', 'down', 'out', 'over', 'under', 'again', 'further', 'then', 'once',
              'et', 'à', 'sont', 'de', 'ou', 'mais', 'un', 'une', 'le', 'la', 'l\'', 'les', 'dans', 'sur', 'à', 'au', 'par', 'pour', 'avec', 'sur', 'contre', 'entre', 'dans', 'à travers', 'pendant', 'avant', 'après', 'au-dessus', 'en dessous de', 'de', 'en haut', 'en bas', 'hors de', 'au-dessus', 'sous', 'encore', 'plus loin', 'puis', 'une fois']

    words = s.split()
    titlecased_words = []
    
    for i, word in enumerate(words):
        if word.lower() in exceptions and i != 0 and i != len(words) - 1:
            titlecased_words.append(word.lower())
        else:
            titlecased_words.append(word.capitalize())
    
    return ' '.join(titlecased_words)

