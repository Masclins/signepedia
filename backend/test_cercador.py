import cercador
import unittest

class ParaulesGuardades(unittest.TestCase):
    paraules = ("ós", "Ós", "conill")

    def test_existeix(self):
        for paraula in self.paraules:
            self.assertEqual(cercador.paraula_existeix(paraula), True)

        self.assertEqual(cercador.paraula_existeix("kjasg"), False)
        self.assertEqual(cercador.paraula_existeix("0d0#"), False)
    
    def test_url(self):
        for paraula in self.paraules:
            self.assertEqual(cercador.url(paraula), "../backend/videos/" + paraula.lower() + ".mp4")

        self.assertEqual(cercador.url("piñoàêü"), "SenseResultat")
        self.assertEqual(cercador.url(""), "SenseResultat")

if __name__ == '__main__':
    unittest.main()
