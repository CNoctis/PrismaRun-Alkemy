import unittest
import funciones

class TestCalculadora(unittest.TestCase):
    """Realiza el test unitario para cada funcion de nuestra calculadora"""

    def test_sumar(self):
        """Testea la función suma"""
        self.assertEqual(funciones.sumar(1, 2), 3)
        self.assertEqual(funciones.sumar(-1, 2), 1)
        self.assertEqual(funciones.sumar(1, 'a'), 'Error en la suma')
        self.assertEqual(funciones.sumar('a', 1), 'Error en la suma')
    
    def test_restar(self):
        """Testea la función restar"""
        self.assertEqual(funciones.restar(1, 2), -1)
        self.assertEqual(funciones.restar(-1, 2), -3)
        self.assertEqual(funciones.restar(1, 'a'), 'Error en la resta')
        self.assertEqual(funciones.restar('a', 1), 'Error en la resta')

    def test_multiplicar(self):
        """Testea la función multiplicar"""
        self.assertEqual(funciones.multiplicar(1, 2), 2)
        self.assertEqual(funciones.multiplicar(-1, 2), -2)
        self.assertEqual(funciones.multiplicar(1, 'a'), 'Error en la multiplicación')
        self.assertEqual(funciones.multiplicar('a', 1), 'Error en la multiplicación')
    
    def test_dividir(self):
        """Testea la función dividir"""
        self.assertEqual(funciones.dividir(1, 2), 0.5)
        self.assertEqual(funciones.dividir(-1, 2), -0.5)
        self.assertEqual(funciones.dividir(1, 'a'), 'Error en la división')
        self.assertEqual(funciones.dividir('a', 1), 'Error en la división')

if __name__ == '__main__':
    unittest.main()