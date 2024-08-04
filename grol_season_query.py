import os  # Import the os module to interact with the operating system
from groq import Groq  # Import the Groq class from the groq module to interact with the Groq API
from collections import Counter  # Used to count occurrences of results
from season_converter import str_season  # MHDM script to convert results to a usable format
from dotenv import load_dotenv  # Import load_dotenv to load environment variables

# The script is working but could be broken down into several questions to improve result

def load_env_file(filepath):
    """
    Manually loads environment variables from a .env file.
    """
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"The .env file at {filepath} was not found.")

    with open(filepath) as file:
        for line in file:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                os.environ[key] = value

def set_groq_api_key():
    """
    Sets the GROQ_API_KEY environment variable to a specific API key.
    This is necessary for authenticating requests to the Groq API.
    """
    load_env_file('.env')  # Load environment variables from .env file
    api_key = os.getenv('GROQ_API_KEY')
    
    if api_key is None:
        raise ValueError("GROQ_API_KEY is not set in the environment variables.")
    
    os.environ['GROQ_API_KEY'] = api_key

def AI_season_query(ingredient, query):
    set_groq_api_key()  # Set the Groq API key
    
    #actual Query
    user_prompt = f'What month is the {query} of {ingredient} season in the UK? No text, just a single number representing the month.'
    
    results = []  # Initialise an empty list to store the results

    for _ in range(7):  # Repeat the query 6 times
        try:
            # Create a Groq client instance with the API key from environment variables
            client = Groq(
                api_key=os.environ.get("GROQ_API_KEY"),
            )
            
            # Create a chat completion request with the user prompt
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",  # Specify the role of the message
                        "content": user_prompt,  # Include the user prompt as the message content
                    }
                ],
                model="llama3-8b-8192",  # Specify the model to use for the chat completion
            )
            
            # Append the response from the API to the results list
            results.append(chat_completion.choices[0].message.content.strip())
        
        except Exception as e:
            # Print an error message if an exception occurs during the API request
            print(f"An error occurred: {e}")

    counter = Counter(results)
    # Find the most common value
    most_common_value, frequency = counter.most_common(1)[0]

    # Return the most common result after processing it with the str_season function
    return str_season(most_common_value)

# Example usage

def auto_ingredient_season(ingredient):
    start = AI_season_query(ingredient, 'start')
    end = AI_season_query(ingredient, 'end')
    return f'{start}-{end}'

#print(auto_ingredient_season('apple'))

def AI_query(query):
    set_groq_API_key()
    results = []
    user_prompt = query