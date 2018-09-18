import requests
from dictionary import search
import db

# Requests the synonyms of a "word" to OpenThesaurus.
# Removes repeated or equal to "word".
def request_synonyms(word):
    try:
        req = requests.get("https://openthesaurus.softcatala.org/synonyme/search?q=" + word + "&format=application/json")
        if req.status_code != 200:
            db.errorLog("request_synonyms", word, req.status_code)
            return []

        defs = req.json()["synsets"]

        synonyms = []
        for def_tmp in defs:
            for ss in def_tmp["terms"]:
                synonym = ss["term"]
                if (synonym != word.lower() and not synonym in synonyms):
                    synonyms.append(synonym)

        return synonyms
    except requests.exceptions.RequestException as err:
        db.errorLog("request_synonyms", word, err)
        return []

# Returns the registered synonyms of a "word".
def get_synonyms(word, cursor):
    synonyms = request_synonyms(word)
    regSynonyms = []
    for synonym in synonyms:
        if search.got_entry(synonym, cursor):
            regSynonyms.append(synonym)

    if regSynonyms:
        return regSynonyms
    return None
