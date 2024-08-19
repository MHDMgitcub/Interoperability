#fix when not solid or liquid


import statistics
from AI_utilities import AI_query

count = 0
max_attempts = 3
ingredient = input('ingredient: ')
flag = 0
   
while count < max_attempts and flag == 0:
    # Prompt the user to determine if the ingredient is a solid or liquid
    
    #adding 'only' helped a lot
    unit_query = f'Is the ingredient {ingredient} considered a solid (1) or a liquid (0)? Reply only with the corresponding number: '
    print(unit_query)
    
    response_1 = AI_query(unit_query)
    print(response_1 + '\n')
 
    if count == max_attempts:
        print("Maximum number of attempts reached. Exiting.")
        break        
    
    try:
        response_1 = int(response_1)
    except ValueError:
        print("Invalid input. Please reply with 1 or 0.")
        count += 1
        continue
     
    mean_attempt = 0        
    while True:
        calorie_counts = []
        unit = '100g' if response_1 == 1 else '100ml'
        
        if mean_attempt >= 3:
            print('AI is not precise enough...')
            flag = 1
            break
            
        while len(calorie_counts) < 3:
            calorie_query = f'What is the calorie count of {unit} of {ingredient}? Reply with only the value: '         
            print(calorie_query)
            
            calorie_count = AI_query(calorie_query)
            print(calorie_count + '\n')
            try:
                value = float(calorie_count)
                calorie_counts.append(value)
            except ValueError:
                print("Invalid input. Please provide a numeric value.")

        if len(calorie_counts) == 3:
            mean_calories = statistics.mean(calorie_counts)
            deviation = statistics.stdev(calorie_counts)
            if deviation / mean_calories < 0.25:  # 25% margin of error                
                mean_calories = int(round(mean_calories))
                if mean_calories < 20:
                    print('Null')
                else:
                    print(f'Average calorie count for {unit} of {ingredient} is {mean_calories:.2f} calories.')
                flag = 1
                break
            else:
                print("Calorie counts vary significantly. Retrying...")
                mean_attempt += 1
                continue        

    count += 1

if count == max_attempts:
    print("Exiting after maximum number of attempts.")
