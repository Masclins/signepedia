import os.path
import csv

def entrada(paraula):
    paraula = paraula.lower();
    with open("diccionari.csv") as diccionariCSV:
        diccionari = csv.DictReader(diccionariCSV)
        for entrada in diccionari:
            if (entrada["paraula"] == paraula):
                return [entrada["url"], entrada["origen"]]

        return ["SenseResultat", ""]
