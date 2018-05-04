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
    paraules = []
    for sinonim in sinonims:
        if cercador.tenim_entrada(sinonim):
            paraules.append(sinonim)

    if len(paraules) == 0:
        return dict(paraula=paraula)
    else:
        return dict(paraula=paraula, sinonims=paraules)

