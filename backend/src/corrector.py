import requests
from src import cercador

# Obtenim la correcció ortogràfica d'una "paraula" a través de LanguageTool.
# Si no hi ha correcció, retornem "None".
# Cal evitar saturar el servidor.

def get_correccio(paraula):
    try:
        req = requests.get("https://languagetool.org/api/v2/check?text=" + paraula + "&language=ca&enabledOnly=false")
        resposta = req.json()["matches"][0]
        missatge = resposta["shortMessage"]
        correccions = resposta["replacements"]
        if (correccions) and missatge == "Error ortogràfic":
            return correccions[0]["value"]
        return None
    except:
        return None

# Retornem un mapa amb la possible correcció d'una "paraula" si la tenim registrada.

def corregeix_paraula(paraula):
    correccio = get_correccio(paraula)
    if correccio != None:
        if cercador.tenim_entrada(correccio):
            return dict(paraula=paraula, correccio=correccio)
    
    return dict(paraula=paraula)
