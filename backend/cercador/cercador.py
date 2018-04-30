import os.path
import csv
from cercador import thesaurus

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

# Fem servir el thesaurus per a cercar els sinonims de 
# la paraula entrada. Retornem, dels sinonims obtinguts,
# les paraules que tenim al nostre diccionari.

def troba_sinonims(paraula):
    sinonims = thesaurus.get_sinonims(paraula)
    paraules = []
    for sinonim in sinonims:
        entrada = obte_entrada(sinonim)
        if entrada != None:
            paraules.append(entrada["paraula"])
    
    return dict(paraula=paraula, sinonims=paraules)

# Convertim la paraula entrada a minuscules per evitar errors de matching
# i retornem la paraula entrada. En cas que no estigui registrada, 
# retornem una llista de sinonims.

def cerca_paraula(paraula):
    entrada = obte_entrada(paraula.lower())
    if entrada != None:
        return entrada
    else:
        return troba_sinonims(paraula.lower())
