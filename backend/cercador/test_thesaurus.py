from cercador import thesaurus
import unittest

class TestCercador(unittest.TestCase):

    ### Tests de thesaurus
    def test_obte_sinonims(self):
        self.assertEqual(thesaurus.get_sinonims("prova"), ["assaig", "experiment", "experimentació", "intent", "provatura", "temptativa", "tempteig", "test", "demostració", "examen"])

if __name__ == '__main__':
    unittest.main()
