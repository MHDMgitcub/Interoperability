import statistics

count = 0
max_attempts = 3
ingredient = 'apple'
flag = 0

awhile count < max_attempts and flag == 0:
    # Prompt the user to determine if the ingredient is a solid or liquid
    response_1 = input(f'Is the ingredient {ingredient} considered a solid (1) or a liquid (0)? Reply with the corresponding number: ')
    
    try:
        response_1 = int(response_1)
    except ValueError:
        print("Invalid input. Please reply with 1 or 0.")
        count += 1
        continue 
    
    mean_attempt = 0
    while mean_attempt < 3:
        if response_1 == 1:
            # For solid ingredients
            calorie_counts = [] # here count starts
            while len(calorie_counts)<3:
                calorie_count = input(f'What is the calorie count of 100g of {ingredient}? Reply with only the value: ')
                try:
                    calorie_counts.append(float(calorie_count))
                except ValueError:
                    print("Invalid input. Please provide a numeric value.")
                
            if len(calorie_counts) == 3:
                mean_calories = statistics.mean(calorie_counts)
                deviation = statistics.stdev(calorie_counts)
                if deviation / mean_calories < 0.25:  # 25% margin of error                
                    mean_calories = int(round(mean_calories))
                    print(f'Average calorie count for 100g of {ingredient} is {mean_calories:.2f} calories.')
                    flag = 1
                    break
                else:
                    print("Calorie counts vary significantly. Retrying...") 
                    mean_attempt += 1
                    # here it fails, I want to throw back to where the counting starts. if it fails like this I want to break out of the whole script.   
    
if count == max_attempts:
    print("Maximum number of attempts reached. Exiting.")
