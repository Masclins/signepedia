from src import signepedia
import unittest

class TestSignepedia(unittest.TestCase):

    #########################
    # Tests retorna_entrada #
    #########################

    # Comprovem que estem retornant totes les entrades com hauríem.
    # No fem més de sinònims ni correcció per evitar enlentir els tests.
    def test_entrada_registrada(self):
        paraules = ("màster", "Sant Just")
        entrades = (dict(paraula="màster",nota="",url="videos/màster.mp4",origen="",autor="Tània"), dict(paraula="sant just",nota="",url="https://www.youtube.com/embed/oawVAxU7wVA",origen="youtube",autor="frosinor85"))

        for paraula, entrada in zip(paraules, entrades):
            self.assertEqual(signepedia.retorna_entrada(paraula), entrada)

    def test_entrada_sinonims(self):
        self.assertEqual(signepedia.retorna_entrada("Roig"), {"paraula": "roig", "sinonims": ["vermell"]})

    def test_entrada_correcio(self):
        self.assertEqual(signepedia.retorna_entrada("Vlau"), {"paraula": "vlau", "correccio": "blau"})

if __name__ == '__main__':
    unittest.main()
