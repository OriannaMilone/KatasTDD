

class FB():
    
    def __init__(self):
        pass
    
    def smart_printer(self, number):
        if isinstance(number, int):
            if ((number % 3) == 0):
                return 'Fizz'
        
            