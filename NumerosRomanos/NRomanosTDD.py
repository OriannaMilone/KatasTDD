import unittest
import Numeros as num

class NRomanosTDD(unittest.TestCase):
    
    def setUp(self):
        self.num_romanos = num.NumerosRomanos()
        
    def test_numeros_basicos(self):
        numeros_transformados = self.num_romanos.conversor_num_cardinales_romanos([1,5,10,50,100,500,1000])
        self.assertEqual(['I', 'V', 'X', 'L', 'C', 'D', 'M'], numeros_transformados)
    
    def test_numeros_basicos2(self):
        numeros_transformados = self.num_romanos.conversor_num_romanos_cardinales(['I', 'V', 'X', 'L', 'C', 'D', 'M'])
        self.assertEqual([1,5,10,50,100,500,1000], numeros_transformados)
    
    # def test_numeros_calculados(self):
    #     numeros_transformados = self.num_romanos.conversor_num_cardinales_romanos([2,3,6,7,8])
    #     self.assertEqual(['II', 'III', 'VI', 'VII', 'VIII'], numeros_transformados)
        
    
if __name__ == '__main__':
    unittest.main()