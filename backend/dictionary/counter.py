# Counts the number of different videoIds.
# Since there will be "", we deacrease it by one.
def get_nVideos(cursor):
    query = "SELECT COUNT(t.c) FROM (SELECT 1 AS C FROM dictionary GROUP BY video) AS t"
    cursor.execute(query)
    return cursor.fetchall()[0]["COUNT(t.c)"]
