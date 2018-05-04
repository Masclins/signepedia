from src import corrector
import unittest

class TestCercador(unittest.TestCase):

    ### Tests de languagetool

    def test_obte_correccio(self):
        self.assertEqual(corrector.get_correccio("clase"), "classe")

    def test_falla(self):
        self.assertEqual(corrector.get_correccio("jksdfjfqp"), None)

    ###########################
    # Tests corregeix_paraula #
    ###########################

    def test_corregeix_paraula(self):
        self.assertEqual(corrector.corregeix_paraula("master"), {"paraula": "master", "correccio": "màster"})

if __name__ == '__main__':
    unittest.main()
