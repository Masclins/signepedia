import requests
from dictionary import search
import db

# Gets the ortographical corrections for a "word".
# Requests it to LanguageTool.
# If there's no correction returns "None".
# Must be careful on doing too many requests to the server.
def request_corrections(word):
    try:
        req = requests.get("https://languagetool.org/api/v2/check?text=" + word + "&language=ca&enabledOnly=false")
        if req.status_code != 200:
            db.errorLog("request_corrections", word, req.status_code)
            return None

        response = req.json()["matches"]
        if not response:
            return None
        response = response[0]

        message = response["shortMessage"]
        replacements = response["replacements"]
        if (replacements) and message == "Error ortogràfic":
            corrections = []
            for replacement in replacements:
                corrections.append(replacement["value"])
            return corrections
        return None
    except requests.exceptions.RequestException as err:
        db.errorLog("request_corrections", word, err)
        return None

# Returns the first possible registered correction.
def get_correction(word, cursor):
    corrections = request_corrections(word)
    if corrections is not None:
        for correction in corrections:
            if search.got_entry(correction, cursor):
                return correction

    return None
