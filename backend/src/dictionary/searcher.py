# Returns whether the word is registered.
def got_entry(word, cnx):
    cursor = cnx.cursor(prepared=True)
    query = "SELECT COUNT(word) FROM dictionary WHERE hex LIKE Hex(LOWER(%s))"
    cursor.execute(query, (word,))
    gotIt = cursor.fetchall()[0][0] != 0
    cursor.close()
    return gotIt

# Cleans an entry:
# - Divides the "alternatives" variable.
# - Removes empty variables.
def clean_entry(entry):
    entry["alternatives"] = entry["alternatives"].split("|")
    for key in list(entry.keys()):
        if entry[key] == "" or entry[key] == [""]:
            del entry[key]
    return entry

# Gets the entry on the dictionary db from a "word".
def get_entry(word, cnx):
    cursor = cnx.cursor(dictionary=True)
    query = "SELECT word, videoId, author, alternatives FROM dictionary WHERE hex LIKE Hex(LOWER(%s))"
    cursor.execute(query, (word,))
    entry = cursor.fetchall()
    cursor.close()
    if entry:
        return clean_entry(entry[0])
    return None
