import os.path
import csv
import requests

def thesaurus(paraula):
    req = requests.get("https://openthesaurus.softcatala.org/synonyme/search?q=" + paraula + "&format=application/json")
    defs = req.json()["synsets"]
    
    sinonims = []
    for def_tmp in defs:
        for ss in def_tmp["terms"]:
            sinonim = ss["term"]
            if (sinonim != paraula and not (sinonim in sinonims)):
                sinonims.append(sinonim)

    return sinonims

def obte_entrada(paraula):
    with open("diccionari.csv") as diccionariCSV:
        diccionari = csv.DictReader(diccionariCSV)
        for entrada in diccionari:
            if (entrada["paraula"] == paraula):
                return entrada

        return None

def troba_sinonims(paraula):
    sinonims = thesaurus(paraula)
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
