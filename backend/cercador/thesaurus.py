import requests

# Busquem a la pagina de thesaurus tots els sinonims de la paraula entrada
# Recorrem el conjunt de termes "terms" on cada "term" es un sinonim
# Retornem una llista de tots els sinonims de la paraula entrada tenint en
# compte que no hi ha repeticions i que tots son diferents a la paraula entrada

def get_sinonims(paraula):
    req = requests.get("https://openthesaurus.softcatala.org/synonyme/search?q=" + paraula + "&format=application/json")
    defs = req.json()["synsets"]
    
    sinonims = []
    for def_tmp in defs:
        for ss in def_tmp["terms"]:
            sinonim = ss["term"]
            if (sinonim != paraula and not (sinonim in sinonims)):
                sinonims.append(sinonim)

    return sinonims
