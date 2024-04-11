

class FB():
    
    def __init__(self):
        pass
    
    def smart_printer(self, number):
        if isinstance(number, int):
            if ((number % 3) == 0) and ((number % 5) == 0):
                return 'FizzBuzz'
            elif ((number % 5) == 0):
                return 'Buzz'
            elif ((number % 3) == 0):
                return 'Fizz'
            else: 
                return number
                
            