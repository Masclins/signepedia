from src import sinonims
import unittest

class TestCercador(unittest.TestCase):

    ### Tests de thesaurus

    # Comprovem que obtenim doncs tots els sinonims de la paraula "prova" sense repeticions

    def test_obte_sinonims(self):
        self.assertEqual(sinonims.get_sinonims("prova"), ["assaig", "experiment", "experimentació", "intent", "provatura", "temptativa", "tempteig", "test", "demostració", "examen"])


    ########################
    # Tests troba_sinonims #
    ########################

    # Comprovem que som capaços de trobar els sinonims de la paraula entrada
    def test_troba_sinonims(self):
        self.assertEqual(sinonims.troba_sinonims("escola"), {"paraula": "escola", "sinonims": ["col·legi","estudi","institut"]})

    def test_no_troba_sinonims(self):
        self.assertEqual(sinonims.troba_sinonims("violeta"), {"paraula": "violeta"})

if __name__ == '__main__':
    unittest.main()
