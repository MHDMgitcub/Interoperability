import statistics
from AI_utilities import AI_query

class QueryResolver:
    def __init__(self, max_attempts):
        self.max_attempts = max_attempts

    def resolve_query(self, exception_type, query):
        attempts = 0
        print('\n' + query)
        while attempts < self.max_attempts:
            try:
                query_result = self._try_resolve(query)
                if query_result is not None:
                    self._handle_result(exception_type, query_result)
                    print(f"~ Attempt {attempts + 1} succeeded ~")
                    return query_result
            except Exception as e:
                print(f"~ Attempt {attempts + 1} failed with error: {e} ~")
            attempts += 1
        0
        raise RuntimeError("~ Query resolution failed after maximum attempts ~")

    def _try_resolve(self, query):
        return AI_query(query)

    def _handle_result(self, exception_type, query_result):
        if exception_type == 'boolean_check':
            if int(query_result) not in (0, 1):
                raise ValueError("Result must be 0 or 1.")
        elif exception_type == 'num_check':
            if isinstance(query_result, str):
                try:                   
                    float(query_result)  # Or use int(query_result) if only integers are expected
                except ValueError:
                    raise TypeError("Query failed to return a number.")
        else:
            raise ValueError("Unknown query type.")
            
class MeanQueryResolver(QueryResolver):
    def __init__(self, max_attempts, list_length, start_deviation):
        super().__init__(max_attempts)
        self.list_length = list_length
        self.start_deviation = start_deviation 
        
    def mean_process(self, query, ingredient, unit):
        result_counts = []
        attempts = 0
        
        while attempts < self.max_attempts:
            while len(result_counts) < self.list_length:
                current_query = query.format(unit=unit, ingredient=ingredient)  # Format query dynamically
                print(current_query)
                
                try:
                    query_result = self.resolve_query('num_check', current_query)
                    result_counts.append(float(query_result))
                except (ValueError, TypeError):
                    print("Invalid input. Please provide a numeric value.")
                    continue
            
            if len(result_counts) == self.list_length:
                mean_result = statistics.mean(result_counts)
                deviation = statistics.stdev(result_counts)
                
                if deviation / mean_result < self.start_deviation:
                    mean_result = int(round(mean_result))
                    return mean_result
                else:
                    print("Results vary significantly. Retrying...")
                    result_counts = []  # Clear results for the next attempt
                    attempts += 1
                    self.start_deviation += 0.05  # Optionally adjust the deviation threshold
                    continue
        
        print("Failed to get consistent results after maximum attempts.")
        return None

 
                     
 # External query variable
query_template = 'What is the calorie count of {unit} of {ingredient}? Reply with only the value: '

# Example usage
calorie_resolver = MeanQueryResolver(max_attempts=3, list_length=3, start_deviation=0.25)
calorie_result = calorie_resolver.mean_process(query=query_template, ingredient='apple', unit='100g')
print(f"Average calorie count: {calorie_result}")

#flag =0
#while flag == 0:
#    ingredient = 'apple' #to be input in final
#    unit_query = f'Is the ingredient {ingredient} considered a solid (1) or a liquid (0)? Reply only with the corresponding number: '
#    unit_runs = 3
#    unit_resolver = QueryResolver(unit_runs)
#    unit_result = unit_resolver.resolve_query('boolean_check', unit_query)
#    
#    while True:              
#        calorie_counts = []        
#        calorie_query = f'What is the calorie count of {unit} of {ingredient}? Reply with only the value: '      
#        calorie_runs = 5
#        calorie_resolver = QueryResolver(calorie_runs)
#        calorie_result = calorie_resolver.resolve_query('num_check', calorie_query)
#        print(f'Result: {calorie_result}')
#        flag = 1
#        break


