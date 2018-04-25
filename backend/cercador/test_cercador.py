import cercador
import unittest

class ParaulesGuardades(unittest.TestCase):

    def test_senseresultat(self):
        self.assertEqual(cercador.entrada("piñoàêü"), "SenseResultat")
        self.assertEqual(cercador.entrada(""), "SenseResultat")

    def test_url(self):
        paraules = ("ós", "Ós", "conill", "lego")
        urls     = ("../backend/videos/ós.mp4", "../backend/videos/ós.mp4", "../backend/videos/conill.mp4", "http://techslides.com/demos/sample-videos/small.webm")

        for paraula, url in zip(paraules, urls):
            self.assertEqual(cercador.entrada(paraula)[0], url)

    def test_origen(self):
        paraules = ("conill", "caure")
        origens  = (None, "youtube")

        for paraula, origen in zip(paraules, origens):
            self.assertEqual(cercador.entrada(paraula)[1], origen)

if __name__ == '__main__':
    unittest.main()
