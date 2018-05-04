import os.path
import csv
import unittest

# Comprovem que totes les entrades del diccionari
# tenen els camps que corresponen

class TestDiccionari(unittest.TestCase):

    def diccionari_correcte(self):
        with open("diccionari.csv") as diccionariCSV:
            diccionari = csv.DictReader(diccionariCSV)
            for entrada in diccionari:
                if not (("paraula" in entrada) and ("nota" in entrada) and ("url" in entrada) and ("origen" in entrada) and ("autor" in entrada)):
                    return False
        return True

    def test_camps(self):
        self.assertTrue(self.diccionari_correcte())
    
if __name__ == '__main__':
    unittest.main()
