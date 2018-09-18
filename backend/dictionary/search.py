# Returns whether the word is registered.
def got_entry(word, cursor):
    query = "SELECT * FROM dictionary WHERE hex LIKE Hex(LOWER(%s)) LIMIT 1"
    cursor.execute(query, (word,))
    cursor.fetchall()
    return cursor.rowcount != 0

# Gets an entry by id.
def get_entry(entryId, cursor):
    query = "SELECT * FROM dictionary WHERE id=%s"
    cursor.execute(query, (entryId,))
    return cursor.fetchall()[0]

# Gets all the entries on the dictionary db from a "word".
# Returns an array with all entries (empty if there's none).
def get_entries(word, cursor):
    query = "SELECT * FROM dictionary WHERE hex LIKE Hex(LOWER(%s)) ORDER BY likes-dislikes DESC"
    cursor.execute(query, (word,))
    return cursor.fetchall()
