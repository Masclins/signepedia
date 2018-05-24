import requests
from src.dictionary import searcher

# Requests the synonyms of a "word" to OpenThesaurus.
# Removes repeated or equal to "word".
def request_synonyms(word):
    try:
        req = requests.get("https://openthesaurus.softcatala.org/synonyme/search?q=" + word + "&format=application/json")
        defs = req.json()["synsets"]
    
        synonyms = []
        for def_tmp in defs:
            for ss in def_tmp["terms"]:
                synonym = ss["term"]
                if (synonym != word.lower() and not (synonym in synonyms)):
                    synonyms.append(synonym)

        return synonyms
    except:
        return []

# Returns the registered synonyms of a "word".
def get_synonyms(word , cnx):
    synonyms = request_synonyms(word)
    regSynonyms = []
    for synonym in synonyms:
        if searcher.got_entry(synonym, cnx):
            regSynonyms.append(synonym)

    if regSynonyms:
        return regSynonyms
    return None
