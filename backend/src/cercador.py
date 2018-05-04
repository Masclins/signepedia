import os.path
import csv

# Comprovem que la paraula entrada esta continguda dins 
# el nostre diccionari. Si ho esta, la retornem.
# En cas contrari no retornem res.

def tenim_entrada(paraula):
    with open("diccionari.csv") as diccionariCSV:
        diccionari = csv.DictReader(diccionariCSV)
        for entrada in diccionari:
            if (entrada["paraula"] == paraula):
                return True

        return False

def obte_entrada(paraula):
    entrada_resultat = None
    alternatives = []
    with open("diccionari.csv") as diccionariCSV:
        diccionari = csv.DictReader(diccionariCSV)
        for entrada in diccionari:
            if entrada["paraula"] == paraula:
                if entrada["nota"] == "":
                    entrada_resultat = entrada
                else:
                    alternatives.append(entrada["nota"])
            elif entrada["paraula"] + " " + entrada["nota"] == paraula:
                return entrada

    if len(alternatives) != 0:
        if entrada_resultat != None:
            entrada_resultat["alternatives"] = alternatives
        else:
            entrada_resultat = dict(paraula=paraula, alternatives=alternatives)
    return entrada_resultat
