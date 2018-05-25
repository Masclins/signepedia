# We create a new unvalidated entry.
# It requires the word, the videoId and the author.
def insert(newEntry, cnx):
    try:
        cursor = cnx.cursor(prepared=True)
        query = "INSERT INTO unvalidated VALUES (NULL, %s, %s, %s)"
        cursor.execute(query, (newEntry["word"], newEntry["videoId"], newEntry["author"]))
        cursor.close()
        cnx.commit()
        return "done"
    except:
        return "fail"

# Called upon validation of an unvalidated entry.
# It moves the entry to the dictionary.
def validate(entry, cnx):
    cursor = cnx.cursor(dictionary=True)
    query = "SELECT videoId FROM unvalidated WHERE id=%s"
    cursor.execute(query, (entry["id"],))
    videoId = cursor.fetchall()[0]["videoId"]
    try:
        query = "INSERT INTO dictionary VALUES (Hex(%s), %s, %s, %s, %s)"
        cursor.execute(query, (entry["word"].lower(), entry["word"], videoId, entry["author"], entry["alternatives"]))
        query = "DELETE FROM unvalidated WHERE id=%s"
        cursor.execute(query, (entry["id"],))
        cursor.close()
        cnx.commit()
        return "done"
    except:
        return "fail"

# Gets the first video yet to validate.
def get_unvalidated(cnx):
    cursor = cnx.cursor(dictionary=True)
    query = "SELECT * FROM unvalidated LIMIT 1"
    cursor.execute(query)
    entry = cursor.fetchall()
    if entry:
        return entry[0]
    return dict(error="empty")
