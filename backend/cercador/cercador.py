import os.path
import csv
from cercador import thesaurus

def obte_entrada(paraula):
    with open("diccionari.csv") as diccionariCSV:
        diccionari = csv.DictReader(diccionariCSV)
        for entrada in diccionari:
            if (entrada["paraula"] == paraula):
                return entrada

        return None

def troba_sinonims(paraula):
    sinonims = thesaurus.get_sinonims(paraula)
    paraules = []
    for sinonim in sinonims:
        entrada = obte_entrada(sinonim)
        if entrada != None:
            paraules.append(entrada["paraula"])
    
    return dict(paraula=paraula, sinonims=paraules)

def cerca_paraula(paraula):
    entrada = obte_entrada(paraula.lower())
    if entrada != None:
        return entrada
    else:
        return troba_sinonims(paraula.lower())
