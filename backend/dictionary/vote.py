import datetime

# Returns whether a user can vote an entry.
def canVote(entryId, userId, cursor):
    query = "SELECT * FROM votes WHERE id_entry=%s AND id_user=%s LIMIT 1"
    cursor.execute(query, (entryId, userId))
    cursor.fetchall()
    if cursor.rowcount != 0:
        return False
    query = "SELECT * FROM dictionary WHERE id=%s AND id_user=%s LIMIT 1"
    cursor.execute(query, (entryId, userId))
    cursor.fetchall()
    if cursor.rowcount != 0:
        return False
    return True

# Register the voting for a video.
def vote(entryId, userId, vote, cursor):
    if canVote(entryId, userId, cursor):
        if vote == "like":
            query = "UPDATE dictionary SET likes=likes+1 WHERE id=%s"
        elif vote == "dislike":
            query = "UPDATE dictionary SET dislikes=dislikes+1 WHERE id=%s"
        else:
            raise Exception("IllegalVoteString")
        cursor.execute(query, (entryId,))

    query = "INSERT INTO votes VALUES (%s, %s, %s, %s)"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    cursor.execute(query, (entryId, userId, vote, now))
