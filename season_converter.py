
# converts strings to ensure its months

def str_season(month):
    month_mapping = {
        "january": 1, "february": 2, "march": 3, "april": 4,
        "may": 5, "june": 6, "july": 7, "august": 8,
        "september": 9, "october": 10, "november": 11, "december": 12
    }
    
    if month.isdigit():
        return int(month)
    
    month_lower = month.lower()
    
    if month_lower in month_mapping:
        return month_mapping[month_lower]
    
    return '1-12'
        


    