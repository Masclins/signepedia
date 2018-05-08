import csv
import unittest

# Comprovem que totes les entrades del diccionari
# tenen els camps que corresponen

class TestDiccionari(unittest.TestCase):

    @classmethod
    def diccionari_correcte(self):
        with open("diccionari.csv") as diccionariCSV:
            diccionari = csv.DictReader(diccionariCSV)
            for entrada in diccionari:
                if not (("paraula" in entrada) and ("nota" in entrada) and ("url" in entrada) and ("origen" in entrada) and ("autor" in entrada)):
                    return False
                if entrada["origen"] != "youtube" and entrada["origen"] != "":
                    return False
                if entrada["autor"] == "":
                    return False
        return True

    def test_camps(self):
        self.assertTrue(self.diccionari_correcte())

if __name__ == '__main__':
    unittest.main()
