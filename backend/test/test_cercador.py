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

    ############################
    # Tests uneix_paraula_nota #
    ############################

    # Comprovem que uneix dues paraules com esperariem
    def test_uneix_paraula_nota(self):
        self.assertEqual(cercador.uneix_paraula_nota("alpha","omega"), "alpha omega")
        self.assertEqual(cercador.uneix_paraula_nota("soleta",""), "soleta")
        self.assertEqual(cercador.uneix_paraula_nota("el","-guió"), "el-guió")
        self.assertEqual(cercador.uneix_paraula_nota("El","'delbar"), "El'delbar")
        self.assertEqual(cercador.uneix_paraula_nota("Why so serious", "?"), "Why so serious?")

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
        urls = ("videos/adreça.mp4", "https://www.youtube.com/embed/LqaR9NO8hmk", "https://www.youtube.com/embed/oawVAxU7wVA", "https://www.youtube.com/embed/XjsjQ_NUYJM", "https://www.youtube.com/embed/VMHoIzjYXt0")
        origens = ("", "youtube", "youtube", "youtube", "youtube")

        for paraula, url, origen in zip(paraules, urls, origens):
            entrada = cercador.obte_entrada(paraula)
            self.assertEqual(entrada["paraula"], paraula)
            self.assertFalse("sinonims" in entrada)
            self.assertFalse("correccio" in entrada)
            self.assertEqual(entrada["origen"], origen)
            self.assertEqual(cercador.obte_entrada(paraula)["url"], url)
 
    def test_obte_entrada_alternatives(self):
        paraules = ("ajudant", "abans")
        alternatives_v = (["ajudant (a la feina)", "ajudant (auxiliar)"],["abans d'ahir"])

        for paraula, alternatives in zip(paraules, alternatives_v):
            self.assertEqual(cercador.obte_entrada(paraula)["alternatives"], alternatives)

    def test_obte_entrada_sense_alternatives(self):
        self.assertFalse("alternatives" in cercador.obte_entrada("abril"))
        
        

if __name__ == '__main__':
    unittest.main()
