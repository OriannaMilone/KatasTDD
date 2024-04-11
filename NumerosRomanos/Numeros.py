

class NumerosRomanos():
        
    def __init__(self):
        self.numeros_base = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M', 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    def conversor_num_cardinales_romanos(self, numeros_cardinales):
        if not isinstance(numeros_cardinales, list):
            numeros_cardinales = list(numeros_cardinales)
        numeros_romanos = []
        for i in numeros_cardinales:
            if i not in self.numeros_base:
                numeros_romanos.append(self.calcular_numero_equivalente(i))
        
            numeros_romanos.append(self.numeros_base[i])
        return numeros_romanos
    
    def conversor_num_romanos_cardinales(self, numeros_romanos):
        if not isinstance(numeros_romanos, list):
            numeros_romanos = list(numeros_romanos)
        numeros_cardinales = []
        for i in numeros_romanos: 
            numeros_cardinales.append(self.numeros_base[i])
        return numeros_cardinales
    
    def calcular_numero_equivalente(self, numero):
        #Pensando en un algoritmo