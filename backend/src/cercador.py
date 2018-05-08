import os.path
import csv

# Retornem si "paraula" esta registrada al diccionari.

def tenim_entrada(paraula):
    with open("diccionari.csv") as diccionariCSV:
        diccionari = csv.DictReader(diccionariCSV)
        for entrada in diccionari:
            if (entrada["paraula"].lower() == paraula.lower()):
                return True

        return False

def uneix_paraula_nota(paraula, nota):
    if nota == "":
        return paraula
    char0 = nota[0]
    if char0 == "-" or char0 == "'" or char0 == "?" or char0 == ",":
        return paraula + nota
    return paraula + " " + nota

# Retornem l'entrada del diccionari, i alternatives, d'una "paraula".

def obte_entrada(paraula):
    entrada_resultat = None
    alternatives = []
    with open("diccionari.csv") as diccionariCSV:
        diccionari = csv.DictReader(diccionariCSV)
        for entrada in diccionari:
            paraula_entrada = uneix_paraula_nota(entrada["paraula"], entrada["nota"])
            if paraula_entrada.lower() == paraula.lower():
                entrada_resultat = entrada
                entrada_resultat["paraula"] = paraula
                del entrada_resultat["nota"]
            elif entrada["paraula"].lower() == paraula.lower():
                alternatives.append(paraula_entrada)

    if alternatives:
        if entrada_resultat != None:
            entrada_resultat["alternatives"] = alternatives
        else:
            entrada_resultat = dict(paraula=paraula, alternatives=alternatives)
    return entrada_resultat
