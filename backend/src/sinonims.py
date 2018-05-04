import requests
from src import cercador

# Busquem a la pagina de thesaurus tots els sinonims de la paraula entrada
# Recorrem el conjunt de termes "terms" on cada "term" es un sinonim
# Retornem una llista de tots els sinonims de la paraula entrada tenint en
# compte que no hi ha repeticions i que tots son diferents a la paraula entrada

def get_sinonims(paraula):
    try:
        req = requests.get("https://openthesaurus.softcatala.org/synonyme/search?q=" + paraula + "&format=application/json")
        defs = req.json()["synsets"]
    
        sinonims = []
        for def_tmp in defs:
            for ss in def_tmp["terms"]:
                sinonim = ss["term"]
                if (sinonim != paraula and not (sinonim in sinonims)):
                    sinonims.append(sinonim)

        return sinonims
    except:
        return []

# Fem servir el thesaurus per a cercar els sinonims de 
# la paraula entrada. Retornem, dels sinonims obtinguts,
# les paraules que tenim al nostre diccionari.

def troba_sinonims(paraula):
    sinonims = get_sinonims(paraula)
    paraules = []
    for sinonim in sinonims:
        entrada = cercador.obte_entrada(sinonim)
        if entrada != None:
            paraules.append(entrada["paraula"])

    if len(paraules) == 0:
        return dict(paraula=paraula)
    else:
        return dict(paraula=paraula, sinonims=paraules)

