import unittest
import fizzbuzzclass as fbc

class FizzBuzzKata(unittest.TestCase):
    
    def setUp(self):
        self.numbers = fbc.FB()

    def test_multiple_of_three(self):
        test_numbers = [3, 6, 9, 12]
        for i in test_numbers: 
            result = self.numbers.smart_printer(i)
            self.assertEqual('Fizz', result)    
    
    def test_multiple_of_five(self):
        test_numbers = [5, 10, 15, 50]
        for i in test_numbers: 
            result = self.numbers.smart_printer(i)
            self.assertEqual('Buzz', result) 
               
    
    
if __name__ == '__main__':
    unittest.main()