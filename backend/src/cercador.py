import os.path
import csv

# Comprovem que la paraula entrada esta continguda dins 
# el nostre diccionari. Si ho esta, la retornem.
# En cas contrari no retornem res.

def obte_entrada(paraula):
    with open("diccionari.csv") as diccionariCSV:
        diccionari = csv.DictReader(diccionariCSV)
        for entrada in diccionari:
            if (entrada["paraula"] == paraula):
                return entrada

        return None
