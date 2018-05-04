import requests
from src import cercador

def get_correccio(paraula):
    try:
        req = requests.get("https://languagetool.org/api/v2/check?text=" + paraula + "&language=ca&enabledOnly=false")
        correccions = req.json()["matches"][0]["replacements"]
        if (len(correccions) == 0):
            return None
        else :
            return correccions[0]["value"]
    except:
        return None

# Fem servir LanguageTool per comprovar si la paraula
# està mal escrita. Retornem l'alternativa si la tenim
# al nostre diccionari.

def corregeix_paraula(paraula):
    correccio = get_correccio(paraula)
    if correccio != None:
        entrada = cercador.obte_entrada(correccio)
        if entrada != None:
            return dict(paraula=paraula, correccio=correccio)
    
    return dict(paraula=paraula)
