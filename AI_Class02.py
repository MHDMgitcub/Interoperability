import statistics
from AI_utilities import AI_query

class Query:
    def __init__(self, cull_list=None):
        self.cull_list = cull_list if cull_list else []

    def resolve(self, query, exception_type = None, max_attempts = 3):
        attempts = 0           
        while attempts < max_attempts:
            try:
                query_result = self._run_query(query)
                if query_result is not None:
                    query_result = self._handle_result(exception_type, query_result)
                    print(f"~ Attempt {attempts + 1} succeeded ~ " + query_result)
                    return query_result
            except Exception as e:
                print(f"~ Attempt {attempts + 1} failed with error: {e} ~ ")
            attempts += 1
        raise RuntimeError("~ Query resolution failed after maximum attempts ~")

    def _run_query(self, query):
        return AI_query(query)
        
    def _handle_result(self, exception_type, query_result):
        if exception_type is None:
            return query_result
        elif exception_type == 'boolean_check':
            if int(query_result) not in (0, 1):
                raise ValueError("Result must be 0 or 1.")
        elif exception_type == 'num_check':
            original_result = query_result
            if isinstance(query_result, str):
                try:
                    float(query_result)           
                except ValueError:
                    query_result = self._cull_strings(query_result)
 
                    try:
                        float(query_result)
                    except ValueError:
                        if '-' in query_result:
                            try:
                                parts = query_result.split('-')
                                query_result = str((float(parts[0]) + float(parts[1]))/2)                              
                            except ValueError:
                                raise TypeError("Query failed to return a number even after culling. ~ " + original_result)
                        else:
                            raise TypeError("Query not a number" + original_result)
                            
        else:
            raise ValueError("Unknown query type.")
        return query_result

    def _cull_strings(self, query_result):
        for item in self.cull_list:
            query_result = query_result.replace(item, "")
        return query_result.strip()

class MeanQuery(Query):
    def __init__(self, cull_list=None):
        super().__init__(cull_list=cull_list)        
        self.list = []
        self.start_deviation = 0.5

    def _list_results(self, list_length, query, exception_type, max_attempts):
        self.list = []  # Reset the list each time        
        while len(self.list) < list_length:
            result = self.resolve(query, exception_type, max_attempts)
            if result is None:
                return None
            self.list.append(float(result))
        return self.list    
            
    def mean_list(self, list_length, query, exception_type, max_attempts):
        while True:
            results = self._list_results(list_length, query, exception_type, max_attempts)                                                          
            if results is None:
                print("No valid results obtained.")
                return None, None  # Return None for both values if list is empty
            
            mean_result = statistics.mean(self.list)
            deviation = statistics.stdev(self.list)
            
            if mean_result == 0:
                return 0, 0
    
            if deviation / mean_result < self.start_deviation:
                var_coeff = int(round(deviation / mean_result * 100 / 5) * 5)
                print(self.list)
                return int(round(mean_result)), var_coeff
            else:
                print(self.list)
                print(f"Results vary significantly with {int(round(self.start_deviation * 100))}% error margin... retrying" + '\n~~~')
                self.start_deviation += 0.5  # Modify this if you want different retry logic

def calorie_processor(ingredient):
    liquid_solid = f'Is the ingredient {ingredient} considered a solid (1) or a liquid (0)? Reply only with the corresponding number: '
    print(liquid_solid)
    
    # Run first query
    cull_cal = ['kcal', 'calories', 'Calories', 'cal', 's', 'kal', 'calorie', 'Calorie', '-kcal', 'kcal/L']
    
    unit_query = Query()             
    unit_result = unit_query.resolve(liquid_solid, 'boolean_check', 3)
    print('~~~')
    unit = '100g' if unit_result == '1' else '100ml' if unit_result == '0' else None
    
    # Run second query
    calorie_count = f'What is the calorie count of {unit} of {ingredient}? Reply with only the value: '
    print(calorie_count)
    
    calorie_query = MeanQuery(cull_list=cull_cal)
    calorie_result, var_coeff = calorie_query.mean_list(5, calorie_count, 'num_check', 15)
    print(f'Result: {calorie_result} with {var_coeff}% margin of error'+'\n\n')  
    return calorie_result, var_coeff
    

def price_estimator(ingredient):
    #what is the typical price of x of x bought at x?
    
    price = f'what is the price per kg of {ingredient} in £. give me a single answer with no description'
    cull_pound = ['£']
    price_query = Query(cull_pound)    
    estimated_price = float(price_query.resolve(price, 'num_check'))
    
    portion = f'what is a standard portion of {ingredient} you can buy at a supermarket to for two in the UK. give me a single answer with no description'
    portion_query = Query()
    estimated_portion = portion_query.resolve(portion)       
    
    conversion = f'what weight in metric does {portion} of {ingredient} correspond to?'
    cull_metric = ['g', 'kg'] 
    conversion_query = Query(cull_metric)
    estimated_conversion = float(conversion_query.resolve(conversion, 'num_check'))
    
    total = estimated_conversion * estimated_price
    return(total)
    
    
  
    
    #think of informin you on the price of large itcket items and get you to check them from the most to the least expensive
 
#ingredient = 'avocadoes'
#print(f'The price of a portion of {ingredient} is £' + price_estimator(ingredient))

