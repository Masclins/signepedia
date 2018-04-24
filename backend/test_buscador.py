import buscador
import unittest

class ParaulesGuardades(unittest.TestCase):
    paraules = ("os", "conill")

    def test_existeix(self):
        for paraula in self.paraules:
            self.assertEqual(buscador.paraula_existeix(paraula), True)

        self.assertEqual(buscador.paraula_existeix("kjasg"), False)
        self.assertEqual(buscador.paraula_existeix("0d0#"), False)
    
    def test_url(self):
        for paraula in self.paraules:
            self.assertEqual(buscador.url(paraula), "../backend/videos/" + paraula + ".mp4")

        self.assertEqual(buscador.url("piñoàêü"), "SenseResultat")
        self.assertEqual(buscador.url(""), "SenseResultat")

if __name__ == '__main__':
    unittest.main()
