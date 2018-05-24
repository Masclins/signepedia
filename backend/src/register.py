# Rgisters the search of a word.
def register_search(word, cnx):
    cursor = cnx.cursor(prepared=True)
    query = "INSERT INTO views VALUES (Hex(%s), %s, 1) ON DUPLICATE KEY UPDATE num=num+1"
    cursor.execute(query, (word, word,))
    cursor.close()
    cnx.commit()
