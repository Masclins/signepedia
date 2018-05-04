import requests

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
