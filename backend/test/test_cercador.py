from src import cercador
import unittest

class TestCercador(unittest.TestCase):

    #######################
    # Tests tenim_entrada #
    #######################

    # Comprovem que respon correctament
    def test_tenim_entrada(self):
        self.assertTrue(cercador.tenim_entrada("zebra"))
        self.assertTrue(cercador.tenim_entrada("cloïssa"))
        self.assertFalse(cercador.tenim_entrada("qkañ"))
        self.assertFalse(cercador.tenim_entrada("brunada"))

    ########################
    # Tests neteja_entrada #
    ########################
    def test_neteja_entrada(self):
        self.assertEqual(
                cercador.neteja_entrada(dict(a="foo", b="", c="bar", alternatives="")),
                dict(a="foo", c="bar"))
        self.assertEqual(
                cercador.neteja_entrada(dict(paraula="Hola", alternatives="Hola què tal?|Bon dia|Hola i adéu")),
                dict(paraula="Hola", alternatives=["Hola què tal?", "Bon dia", "Hola i adéu"]))

    ######################
    # Tests obte_entrada #
    ######################

    # Comprovem que una entrada no registrada no retorna res.
    def test_obte_senseresultat(self):
        self.assertEqual(cercador.obte_entrada("bermell"), None)
        self.assertEqual(cercador.obte_entrada(""), None)
        self.assertEqual(cercador.obte_entrada("¿ ?"), None)

    # Comprovem que el matching de la paraula amb diferents paràmetres de l'entrada és correcte.
    def test_obte_entrada(self):
        paraules = ("adreça", "1.000", "sant just", "ajudar-me", "abans")
        paraulesReg = ("adreça", "1.000", "Sant Just", "ajudar-me", "abans")
        videoIds = ("M87iZZTgeRw", "LqaR9NO8hmk", "oawVAxU7wVA", "XjsjQ_NUYJM", "VMHoIzjYXt0")

        for paraula, paraulaReg, videoId in zip(paraules, paraulesReg, videoIds):
            entrada = cercador.obte_entrada(paraula)
            self.assertEqual(entrada["paraula"], paraulaReg)
            self.assertFalse("sinonims" in entrada)
            self.assertFalse("correccio" in entrada)
            self.assertEqual(cercador.obte_entrada(paraula)["videoId"], videoId)

    def test_obte_entrada_alternatives(self):
        paraules = ("AJUDANT", "abans", "amèrica")
        alternatives_v = (["ajudant (a la feina)", "ajudant (auxiliar)"], ["abans d'ahir"], ["americà", "Amèrica (continent)", "Amèrica central", "Amèrica del nord", "Amèrica del sud"])

        for paraula, alternatives in zip(paraules, alternatives_v):
            self.assertEqual(cercador.obte_entrada(paraula)["alternatives"], alternatives)

    def test_obte_entrada_sense_alternatives(self):
        self.assertFalse("alternatives" in cercador.obte_entrada("abril"))

if __name__ == '__main__':
    unittest.main()
