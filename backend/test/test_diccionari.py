import csv
import unittest
from src import cercador

# Comprovem que totes les entrades del diccionari
# tenen els camps que corresponen

class TestDiccionari(unittest.TestCase):

    @staticmethod
    def diccionari_correcte():
        with open("diccionari.csv") as diccionariCSV:
            diccionari = csv.DictReader(diccionariCSV)
            for entrada in diccionari:
                if entrada["url"] == "" or entrada["autor"] == "":
                    if entrada["alternatives"] == "":
                        return False
                for alternativa in entrada["alternatives"].split("|"):
                    if alternativa != "" and cercador.tenim_entrada(alternativa) is None:
                        print(entrada, alternativa)
                        return False
        return True

    def test_diccionari(self):
        self.assertTrue(self.diccionari_correcte())

if __name__ == '__main__':
    unittest.main()
