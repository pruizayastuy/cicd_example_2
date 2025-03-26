import unittest

from es_primo import es_primo


class TestPrimos(unittest.TestCase):

    def test_negativos_y_cero(self):
        self.assertEqual(es_primo(-5), 'No es posible devolver números primos.')
        self.assertFalse(es_primo(0))

    def test_numeros_pequenos(self):
        self.assertFalse(es_primo(1))
        self.assertTrue(es_primo(2))
        self.assertTrue(es_primo(3))

    def test_pares_mayores_a_dos(self):
        self.assertFalse(es_primo(4))
        self.assertFalse(es_primo(10))
        self.assertFalse(es_primo(100))

    def test_primos_conocidos(self):
        self.assertTrue(es_primo(5))
        self.assertTrue(es_primo(7))
        self.assertTrue(es_primo(13))
        self.assertTrue(es_primo(29))

    def test_compuestos(self):
        self.assertFalse(es_primo(9))
        self.assertFalse(es_primo(15))
        self.assertFalse(es_primo(21))
        self.assertFalse(es_primo(35))

    def test_numeros_grandes(self):
        self.assertTrue(es_primo(97))
        self.assertFalse(es_primo(1000))
        self.assertTrue(es_primo(104729))  # Número primo grande


if __name__ == '__main__':
    unittest.main()
