from cercador import thesaurus
import unittest

class TestCercador(unittest.TestCase):

    ### Tests de thesaurus

    # Comprovem que obtenim doncs tots els sinonims de la paraula "prova" sense repeticions

    def test_obte_sinonims(self):
        self.assertEqual(thesaurus.get_sinonims("prova"), ["assaig", "experiment", "experimentació", "intent", "provatura", "temptativa", "tempteig", "test", "demostració", "examen"])

if __name__ == '__main__':
    unittest.main()
