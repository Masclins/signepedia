from src import signepedia
import unittest

class TestSignepedia(unittest.TestCase):

    #########################
    # Tests retorna_entrada #
    #########################

    # Comprovem que estem retornant totes les entrades com hauríem.
    # No fem més de sinònims ni correcció per evitar enlentir els tests.
    def test_entrada_registrada(self):
        paraules = ("Màster", "sant jordi")
        entrades = (dict(paraula="màster",url="videos/màster.mp4",autor="Tània Tebé"), dict(paraula="Sant Jordi",url="https://www.youtube.com/embed/CG_5OFGV4NI",autor="generalitat"))

        for paraula, entrada in zip(paraules, entrades):
            self.assertEqual(signepedia.retorna_entrada(paraula), entrada)

    def test_entrada_alternatives(self):
        paraules = ("abans", "amèrica")
        entrades = (dict(paraula="abans",url="https://www.youtube.com/embed/VMHoIzjYXt0",autor="frosinor85",alternatives=["abans d'ahir"]), dict(paraula="Amèrica",alternatives=["Amèrica (continent)","Amèrica central","Amèrica del nord","Amèrica del sud"]))

        for paraula, entrada in zip(paraules, entrades):
            self.assertEqual(signepedia.retorna_entrada(paraula), entrada)

    def test_entrada_sinonims(self):
        self.assertEqual(signepedia.retorna_entrada("Roig"), {"paraula": "Roig", "sinonims": ["vermell"]})

    def test_entrada_correcio(self):
        self.assertEqual(signepedia.retorna_entrada("Vlau"), {"paraula": "Vlau", "correccio": "blau"})

if __name__ == '__main__':
    unittest.main()
