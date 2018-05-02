from cercador import cercador
import unittest

class TestCercador(unittest.TestCase):
    
    #########################
    # Tests de obte_entrada #
    #########################

    # Comprovem que un conjunt buit aixi com una entrada erronia no retorna res
    def test_obte_senseresultat(self):
        self.assertEqual(cercador.obte_entrada("piñoàêü"), None)
        self.assertEqual(cercador.obte_entrada(""), None)
        self.assertEqual(cercador.obte_entrada("Sant Jordi"), None)

    # Comprovem que el matching de la paraula amb la seva url es duu a terme correctament
    def test_obte_entrada_url(self):
        paraules = ("adreça", "1.000", "sant just")
        urls     = ("../videos/adreça.mp4", "https://www.youtube.com/embed/LqaR9NO8hmk", "https://www.youtube.com/embed/oawVAxU7wVA")

        for paraula, url in zip(paraules, urls):
            self.assertEqual(cercador.obte_entrada(paraula)["url"], url)
 
    def test_obte_entrada_origen(self):
        paraules = ("horari", "pèsol")
        origens  = ("", "youtube")

        for paraula, origen in zip(paraules, origens):
            self.assertEqual(cercador.obte_entrada(paraula)["origen"], origen)

    ########################
    # Tests troba_sinonims #
    ########################

    # Comprovem que som capaços de trobar els sinonims de la paraula entrada
    def test_troba_sinonims(self):
        self.assertEqual(cercador.troba_sinonims("escola"), {"paraula": "escola", "sinonims": ["col·legi","estudi","institut"]})

    #######################
    # Tests cerca_paraula #
    #######################

    def test_cerca_paraula_url(self):
        paraules = ("màster", "Sant Just")
        urls     = ("../videos/màster.mp4", "https://www.youtube.com/embed/oawVAxU7wVA")

        for paraula, url in zip(paraules, urls):
            self.assertEqual(cercador.cerca_paraula(paraula)["url"], url)

    def test_cerca_paraula_sinonims(self):
        self.assertEqual(cercador.cerca_paraula("Roig"), {"paraula": "roig", "sinonims": ["vermell"]})

if __name__ == '__main__':
    unittest.main()
