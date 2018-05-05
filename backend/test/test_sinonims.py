from src import sinonims
import unittest

class TestSinonims(unittest.TestCase):

    ######################
    # Tests get_sinonims #
    ######################

    # Comprovem que obtenim tots els sinonims sense repeticions.
    # No en fem més per evitar enlentir les proves.

    def test_get_sinonims(self):
        self.assertEqual(sinonims.get_sinonims("prova"), ["assaig", "experiment", "experimentació", "intent", "provatura", "temptativa", "tempteig", "test", "demostració", "examen"])


    ########################
    # Tests troba_sinonims #
    ########################

    # Comprovem que retornem només els sinònims registrats.
    # No en fem més per evitar enlentir les proves.

    def test_troba_sinonims(self):
        self.assertEqual(sinonims.troba_sinonims("escola"), {"paraula": "escola", "sinonims": ["col·legi","estudi","institut"]})

    def test_no_troba_sinonims(self):
        self.assertEqual(sinonims.troba_sinonims("llamp"), {"paraula": "llamp"})

if __name__ == '__main__':
    unittest.main()
