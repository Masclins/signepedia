from dictionary import search
from dictionary import synonyms
from dictionary import corrector
from dictionary import counter

# Searches all the info that has to be passed.
# Creates an entry passing:
# 1- Entry for the "word"
# 2- Synonyms for the "word"
# 3- (If 1 and 2 are empty) Orthographical correction.
def get_result(word, cursor):
    result = dict(word=word, nVideos=counter.get_nVideos(cursor))

    entries = search.get_entries(word, cursor)
    if entries:
        result["entries"] = entries

    foundSynonyms = synonyms.get_synonyms(word, cursor)
    if foundSynonyms:
        result["synonyms"] = foundSynonyms

    if "entries" in result or "synonyms" in result:
        return result

    correction = corrector.get_correction(word, cursor)
    if correction:
        result["correction"] = correction

    return result

# Returns the same info as get_result + votes casted for each entry.
def get_result_user(word, userId, cursor):
    result = get_result(word, cursor)

    if "entries" in result:
        for entry in result["entries"]:
            if entry["id_user"] == userId:
                entry["vote"] = "owner"
            else:
                query = "SELECT vote FROM votes WHERE id_entry=%s AND id_user=%s LIMIT 1"
                cursor.execute(query, (entry["id"], userId))
                voteRow = cursor.fetchall()
                if voteRow:
                    entry["vote"] = voteRow[0]["vote"]

    return result
