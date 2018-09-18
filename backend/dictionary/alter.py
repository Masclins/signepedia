import datetime

# We create a new unvalidated entry.
# It requires the word, the videoId and the author.
def insert(newEntry, cursor):
    query = "INSERT INTO dictionary VALUES (NULL, %s, Hex(%s), %s, %s, %s, %s, %s, 0, 0, 0)"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    cursor.execute(
        query, (
            newEntry["word"],
            newEntry["word"],
            newEntry["video"],
            newEntry["idUser"],
            newEntry["comment"],
            now,
            now))

# Called upon validation of an unvalidated entry.
# It makes it valid
def validate(entryId, cursor):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    query = "UPDATE dictionary SET valid=1, date_updated=%s WHERE id=%s"
    cursor.execute(query, (now, entryId))

# Gets all the videos yet to validate.
def get_unvalidated(cursor):
    query = "SELECT * FROM dictionary WHERE valid=0"
    cursor.execute(query)
    return cursor.fetchall()

# Edits an entry.
def edit_entry(entryId, edits, cursor):
    query = "UPDATE dictionary SET word=%s, comment=%s, video=%s, date_updated=%s, valid=1 WHERE id=%s"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    cursor.execute(query, (edits["word"], edits["comment"], edits["video"], now, entryId))

# Deletes an entry from de dictionary and moves it to the graveyard.
def delete_entry(entryId, cursor):
    query = "INSERT INTO dictionary_graveyard SELECT * FROM dictionary WHERE id=%s"
    cursor.execute(query, (entryId,))
    query = "DELETE FROM dictionary WHERE id=%s"
    cursor.execute(query, (entryId,))
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    query = "UPDATE dictionary_graveyard SET date_updated=%s WHERE id=%s"
    cursor.execute(query, (now, entryId))
