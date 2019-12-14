import unittest
import kalkulator

class testy_kalkulator(unittest.TestCase):

    def test_dodawanie(self):
        wynik = kalkulator.dodaj(2,3)
        self.assertEqual(wynik, 5)
        self.assertNotEqual(wynik,2)

    def test_odejmowanie(self):
        wynik = kalkulator.odejmij(5,3)
        self.assertEqual(wynik,2)

    def test_mnozenie(self):
        wynik = kalkulator.iloczyn(5,3)
        self.assertEqual(wynik,15)

    def test_dzielenie(self):
        wynik = kalkulator.iloraz(6,3)
        self.assertEqual(wynik,2)

if __name__ == '__main__':
    unittest.main()
