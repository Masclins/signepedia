import requests
from src.dictionary import searcher

# Gets the ortographical corrections for a "word".
# Requests it to LanguageTool.
# If there's no correction returns "None".
# Must be careful on doing too many requests to the server.
def request_corrections(word):
    try:
        req = requests.get("https://languagetool.org/api/v2/check?text=" + word + "&language=ca&enabledOnly=false")
        response = req.json()["matches"][0]
        message = response["shortMessage"]
        replacements = response["replacements"]
        if (replacements) and message == "Error ortogràfic":
            corrections = []
            for replacement in replacements:
                corrections.append(replacement["value"])
            return corrections
        return None
    except:
        return None

# Returns the first possible registered correction.
def get_correction(word, cnx):
    corrections = request_corrections(word)
    if corrections is not None:
        for correction in corrections:
            if searcher.got_entry(correction, cnx):
                return dict(word=word, correction=correction)
    
    return dict(word=word)
