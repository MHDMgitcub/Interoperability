import statistics
from AI_utilities import AI_query

class Query:
    #simple class to run queries and manage errors)
    def resolve(self, query, exception_type, max_attempts):
        attempts = 0           
        while attempts < max_attempts:
            try:
                query_result = self._run_query(query)
                if query_result is not None:
                    self._handle_result(exception_type, query_result)
                    print(f"~ Attempt {attempts + 1} succeeded ~" + query_result)
                    return query_result
            except Exception as e:
                print(f"~ Attempt {attempts + 1} failed with error: {e} ~" + query_result)
                pass
            attempts += 1
        raise RuntimeError("~ Query resolution failed after maximum attempts ~")

    
    def _run_query(self, query):
        return AI_query(query)
        
    def _handle_result(self, exception_type, query_result):
            if exception_type == 'boolean_check':
                if int(query_result) not in (0, 1):
                    raise ValueError("Result must be 0 or 1.")
            elif exception_type == 'num_check':
                if isinstance(query_result, str):
                    try:                   
                        float(query_result) 
                    except ValueError:
                        raise TypeError("Query failed to return a number.")
            else:
                raise ValueError("Unknown query type.")       
        
class MeanQuery(Query):
    #Enhancement of the query class for less static results
    def __init__(self):
        super().__init__()        
        self.list = []

    def _list_results(self, list_length, query, exception_type, max_attempts):
        self.list = []  # Reset the list each time        
        while len(self.list) < list_length:
            result = self.resolve(query, exception_type, max_attempts)
            if result is None:
                return None
            self.list.append(float(result))
        return self.list    
            
    def mean_list(self, list_length, start_deviation, query, exception_type, max_attempts):
        while True:
            results = self._list_results(list_length, query, exception_type, max_attempts)                                                          
            if results is None:
                print("No valid results obtained.")
                return None, None  # Return None for both values if list is empty
            
            mean_result = statistics.mean(self.list)
            deviation = statistics.stdev(self.list)
            
            if mean_result == 0:
                return 0, 0
    
            if deviation / mean_result < start_deviation:
                start_deviation = int(round(start_deviation*100))
                print(self.list)
                return int(round(mean_result)), start_deviation
            else:
                print(self.list)
                print(f"Results vary significantly with {int(round(start_deviation * 100))}% error margin... retrying" + '\n')
                start_deviation += 0.1  # Modify this if you want different retry logic
                        
def calorie_processor(ingredient):
    liquid_solid = f'Is the ingredient {ingredient} considered a solid (1) or a liquid (0)? Reply only with the corresponding number: '     
    print(liquid_solid)
    
    # run first query
    unit_query = Query()             
    unit_result = unit_query.resolve(liquid_solid, 'boolean_check', 3)   
    print('\n')
    unit = '100g' if unit_result == '1' else '100ml' if unit_result == '0' else None
    
    #run second query
    calorie_count = f'What is the calorie count of {unit} of {ingredient}? Reply with only the value: '
    print(calorie_count)
    
    calorie_query = MeanQuery()
    calorie_result, deviation = calorie_query.mean_list(5, 0.1, calorie_count, 'num_check', 6)
    print(f'Result: {calorie_result} with {deviation}% margin of error')  
    return calorie_result, deviation
    

    
    