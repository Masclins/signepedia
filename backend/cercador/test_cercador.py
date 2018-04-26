from cercador import cercador
import unittest

class TestCercador(unittest.TestCase):

    def test_senseresultat(self):
        self.assertEqual(cercador.entrada("piñoàêü")[0], "SenseResultat")
        self.assertEqual(cercador.entrada("")[0], "SenseResultat")

    def test_url(self):
        paraules = ("Helicòpter", "helicòpter", "cloïssa", "0", "Sant Jordi")
        urls     = ("https://www.youtube.com/embed/hQ6splo5GjQ", "https://www.youtube.com/embed/hQ6splo5GjQ", "https://www.youtube.com/embed/MaIVe1JtVmg", "https://www.youtube.com/embed/fnbDGumgny8", "https://www.youtube.com/embed/CG_5OFGV4NI")

        for paraula, url in zip(paraules, urls):
            self.assertEqual(cercador.entrada(paraula)[0], url)

    def test_origen(self):
        paraules = ("crispetes", "Pèsol")
        origens  = ("youtube", "youtube")

        for paraula, origen in zip(paraules, origens):
            self.assertEqual(cercador.entrada(paraula)[1], origen)

    def test_thesaurus(self):
        self.assertEqual(cercador.thesaurus("prova"), "existeix")
        self.assertEqual(cercador.thesaurus("kkajn"), "no existeix")

if __name__ == '__main__':
    unittest.main()
