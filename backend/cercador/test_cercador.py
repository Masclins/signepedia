from cercador import cercador
import unittest

class TestCercador(unittest.TestCase):

    ### Tests de obte_entrada    
    def test_obte_senseresultat(self):
        self.assertEqual(cercador.obte_entrada("piñoàêü"), None)
        self.assertEqual(cercador.obte_entrada(""), None)
        self.assertEqual(cercador.obte_entrada("Sant Jordi"), None)

    def test_obte_entrada_url(self):
        paraules = ("helicòpter", "cloïssa", "0", "sant jordi")
        urls     = ("https://www.youtube.com/embed/hQ6splo5GjQ", "https://www.youtube.com/embed/MaIVe1JtVmg", "https://www.youtube.com/embed/fnbDGumgny8", "https://www.youtube.com/embed/CG_5OFGV4NI")

        for paraula, url in zip(paraules, urls):
            self.assertEqual(cercador.obte_entrada(paraula)["url"], url)

    def test_obte_entrada_origen(self):
        paraules = ("crispetes", "pèsol")
        origens  = ("youtube", "youtube")

        for paraula, origen in zip(paraules, origens):
            self.assertEqual(cercador.obte_entrada(paraula)["origen"], origen)

    ###Tests troba_sinonims
    def test_troba_sinonims(self):
        self.assertEqual(cercador.troba_sinonims("roig"), {"paraula": "roig", "sinonims": ["vermell"]})

    ###Tests cerca_paraula
    def test_cerca_paraula_url(self):
        paraules = ("helicòpter", "Sant Jordi")
        urls     = ("https://www.youtube.com/embed/hQ6splo5GjQ", "https://www.youtube.com/embed/CG_5OFGV4NI")

        for paraula, url in zip(paraules, urls):
            self.assertEqual(cercador.cerca_paraula(paraula)["url"], url)

    def test_cerca_paraula_sinonims(self):
        self.assertEqual(cercador.cerca_paraula("Roig"), {"paraula": "roig", "sinonims": ["vermell"]})

if __name__ == '__main__':
    unittest.main()
