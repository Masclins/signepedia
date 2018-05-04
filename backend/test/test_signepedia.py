from src import signepedia
import unittest

class TestCercador(unittest.TestCase):
 
    #######################
    # Tests cerca_paraula #
    #######################

    def test_entrada_url(self):
        paraules = ("màster", "Sant Just")
        urls     = ("videos/màster.mp4", "https://www.youtube.com/embed/oawVAxU7wVA")

        for paraula, url in zip(paraules, urls):
            self.assertEqual(signepedia.retorna_entrada(paraula)["url"], url)

    def test_entrada_sinonims(self):
        self.assertEqual(signepedia.retorna_entrada("Roig"), {"paraula": "roig", "sinonims": ["vermell"]})

    def test_entrada_correcio(self):
        self.assertEqual(signepedia.retorna_entrada("Vlau"), {"paraula": "vlau", "correccio": "blau"})

if __name__ == '__main__':
    unittest.main()
