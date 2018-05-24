from src.dictionary import searcher
from src.dictionary import synonyms
from src.dictionary import corrector

# Removes useless keys.
# Also removes "synonyms" already on "alternatives"
def clean_entry(entry):
    if not "alternatives" in entry or not "synonyms" in entry:
        return entry
    for s in entry["synonyms"][:]:
        if s in entry["alternatives"]:
            entry["synonyms"].remove(s)
    if not entry["synonyms"]:
        del entry["synonyms"]
    return entry

# Searchs all the info that has to be passed.
# Creates an entry passing:
# 1- Entry for the "word"
# 2- Alternatives to the "word"
# 3- Synonyms for the "word"
# 4- (If 1, 2 and 3 are empty) Orthographical correction.
def get_entry(word, cnx):
    entry = searcher.get_entry(word, cnx)
    foundSynonyms = synonyms.get_synonyms(word, cnx)
    if entry is None and foundSynonyms is not None:
        return dict(word=word, synonyms=foundSynonyms)
    elif entry is not None:
        if foundSynonyms is not None:
            entry["synonyms"] = foundSynonyms
        return clean_entry(entry)
    return corrector.get_correction(word, cnx)
