from cercador import languagetool
import unittest

class TestCercador(unittest.TestCase):

    ### Tests de languagetool

    def test_obte_correccio(self):
        self.assertEqual(languagetool.get_correccio("clase"), "classe")

    def test_falla(self):
        self.assertEqual(languagetool.get_correccio("jksdfjfqp"), None)

if __name__ == '__main__':
    unittest.main()
