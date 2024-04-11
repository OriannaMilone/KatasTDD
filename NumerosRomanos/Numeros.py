

class NumerosRomanos():
        
    def __init__(self):
        self.numeros_base = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    
    def conversor_num_cardinales_romanos(self, numeros_cardinales):
        if not isinstance(numeros_cardinales, list):
            numeros_cardinales = list(numeros_cardinales)
        numeros_romanos = []
        for i in numeros_cardinales: 
            numeros_romanos.append(self.numeros_base[i])
        return numeros_romanos