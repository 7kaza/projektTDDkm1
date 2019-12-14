import unittest
import hello

class test_wyswietl_tekst(unittest.TestCase):

    def test_hello(self):
        wynik = hello.zwroc_hello_world('Hello world')
        self.assertEqual(wynik,'Hello world')
    if True:
        print('Hello world')

if __name__ == '__main__':
    unittest.main()
