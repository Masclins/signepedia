import requests
from src import cercador

# Obtenim les correccions ortogràfiques d'una "paraula" a través de LanguageTool.
# Si no hi ha correcció, retornem "None".
# Cal evitar saturar el servidor.

def get_correccio(paraula):
    try:
        req = requests.get("https://languagetool.org/api/v2/check?text=" + paraula + "&language=ca&enabledOnly=false")
        resposta = req.json()["matches"][0]
        missatge = resposta["shortMessage"]
        correccions = resposta["replacements"]
        if (correccions) and missatge == "Error ortogràfic":
            paraules = []
            for correccio in correccions:
                paraules.append(correccio["value"])
            return paraules
        return None
    except:
        return None

# Retornem un mapa amb la possible correcció d'una "paraula" si la tenim registrada.

def corregeix_paraula(paraula):
    correccions = get_correccio(paraula)
    if correccions is not None:
        for correccio in correccions:
            paraula_correcte =  cercador.tenim_entrada(correccio)
            if paraula_correcte is not None:
                return dict(paraula=paraula, correccio=paraula_correcte)
    
    return dict(paraula=paraula)
