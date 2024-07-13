import os  # Import the os module to interact with the operating system
from groq import Groq  # Import the Groq class from the groq module to interact with the Groq API
from collections import Counter #used to get member from AI set
from season_converter import str_season #MHDM script to secularism from output

def set_groq_api_key():
    """
    Sets the GROQ_API_KEY environment variable to a specific API key.
    This is necessary for authenticating requests to the Groq API.
    """
    os.environ['GROQ_API_KEY'] = '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'

def get_groq_api_key():
    """
    Retrieves the GROQ_API_KEY environment variable.
    Returns a message indicating whether the API key is set.
    """
    groq_api_key = os.getenv('GROQ_API_KEY')  # Get the GROQ_API_KEY environment variable
    if groq_api_key is None:
        return 'GROQ_API_KEY is not set'  # Return this message if the API key is not set

def AI_season_query(ingredient, query):
    if __name__ == "__main__":
        set_groq_api_key()  # Set the Groq API key    
        
        user_prompt = f'what month is the {query} of {ingredient} eating season in the UK ? no text, just a single number representing the month'
        
        results = []  # Initialise an empty list to store the results
    
        for _ in range(6):  # Repeat the query 6 times
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
                results.append(chat_completion.choices[0].message.content)
            
            except Exception as e:
                # Print an error message if an exception occurs during the API request
                print(f"An error occurred: {e}")
        
        counter = Counter(results)
        # Find the most common value
        most_common_value, frequency = counter.most_common(1)[0]
    
        # Print the results list using the custom script to clean data
        return str_season(most_common_value)
        
print(AI_season_query('pasta', 'start'))
print(AI_season_query('pasta', 'end'))
i = 0
while i < len(results):
  print(results[i])
  i = i + 1

    