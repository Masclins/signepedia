import requests
from src import cercador

# Busquem a OpenThesaurus tots els sinònims d'una "paraula".
# N'eliminem els repetits o iguals a la "paraula".

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

# Retornem un mapa amb els sinonims que tenims registrats d'una "paraula", si n'hi ha algún.

def troba_sinonims(paraula):
    sinonims = get_sinonims(paraula)
    sinonimsRegistrats = []
    for sinonim in sinonims:
        sinonimRegistrat = cercador.tenim_entrada(sinonim)
        if sinonimRegistrat != None:
            sinonimsRegistrats.append(sinonimRegistrat)

    if sinonimsRegistrats:
        return dict(paraula=paraula, sinonims=sinonimsRegistrats)
    return dict(paraula=paraula)
