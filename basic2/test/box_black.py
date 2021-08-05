import unittest

def suma(value1 , value2):
    return value1 + value2

class CajaNegraTest(unittest.TestCase):

    def test_suma_dos_positivos(self):
        numero1 = 10
        numero2 = 5
        resultado = suma(numero1,numero2)
        self.assertEqual(resultado , 15)
    
    def test_suma_negativos(self):
        numero1 = -10
        numero2 = -7
        resultado =  suma(numero1,numero2)
        self.assertEqual(resultado , -17)

if __name__ == '__main__':
    unittest.main()