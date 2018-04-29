import requests

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
