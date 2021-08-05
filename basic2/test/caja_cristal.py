import unittest
from unittest import result

def es_mayor_de_edad(edad):
    if edad >=18:
        return True
    else:
        return False

class PruebaDeCristal(unittest.TestCase):
    def test_mayor_edad(self):
        resultado =  es_mayor_de_edad(20)
        self.assertEqual(resultado,True)

    def test_menos_edad(self):
        result = es_mayor_de_edad(15)
        self.assertEqual(result,False)

    def test_18(self):
        result = es_mayor_de_edad(18)
        self.assertEqual(result,True)

if __name__ == '__main__':
    unittest.main()