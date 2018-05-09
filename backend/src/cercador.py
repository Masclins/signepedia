import os.path
import csv

# Retornem si "paraula" esta registrada al diccionari.

def tenim_entrada(paraula):
    with open("diccionari.csv") as diccionariCSV:
        diccionari = csv.DictReader(diccionariCSV)
        for entrada in diccionari:
            if (entrada["paraula"].lower() == paraula.lower()):
                return entrada["paraula"]

        return None

# Retornem una entrada netejant la informació:
# - Dividim el camp "alternatives".
# - Eliminem els camps buits.

def neteja_entrada(entrada):
    entrada["alternatives"] = entrada["alternatives"].split("|")
    for key in list(entrada.keys()):
        if entrada[key] == "" or entrada[key] == [""]:
            del entrada[key]
    return entrada

# Retornem l'entrada del diccionari, d'una "paraula".

def obte_entrada(paraula):
    with open("diccionari.csv") as diccionariCSV:
        diccionari = csv.DictReader(diccionariCSV)
        for entrada in diccionari:
            if entrada["paraula"].lower() == paraula.lower():
                return neteja_entrada(entrada)

    return None
