import os.path
import csv
import requests

def thesaurus(paraula):
    req = requests.get("https://openthesaurus.softcatala.org/synonyme/search?q=" + paraula + "&format=application/json")
    defs = req.json()["synsets"]
    if (len(defs) > 0):
        return "existeix"
    else:
        return "no existeix"

def entrada(paraula):
    paraula = paraula.lower();
    with open("diccionari.csv") as diccionariCSV:
        diccionari = csv.DictReader(diccionariCSV)
        for entrada in diccionari:
            if (entrada["paraula"] == paraula):
                return [entrada["url"], entrada["origen"]]

        return ["SenseResultat", ""]
