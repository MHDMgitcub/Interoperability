
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
    
def damerau_levenshtein(s1, s2):
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    
    # Create a 2D array to store the distances
    d = [[0] * (lenstr2 + 1) for _ in range(lenstr1 + 1)]
    
    for i in range(lenstr1 + 1):
        d[i][0] = i
    for j in range(lenstr2 + 1):
        d[0][j] = j

    for i in range(1, lenstr1 + 1):
        for j in range(1, lenstr2 + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            
            d[i][j] = min(
                d[i - 1][j] + 1,    # Deletion
                d[i][j - 1] + 1,    # Insertion
                d[i - 1][j - 1] + cost  # Substitution
            )

            # Check for transpositions
            if i > 1 and j > 1 and s1[i - 1] == s2[j - 2] and s1[i - 2] == s2[j - 1]:
                d[i][j] = min(d[i][j], d[i - 2][j - 2] + cost)  # Transposition

    return d[lenstr1][lenstr2]
    



