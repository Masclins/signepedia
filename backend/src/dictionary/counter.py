# Counts the number of different videoIds.
# Since there will be "", we deacrease it by one.
def videoIds(cnx):
    cursor = cnx.cursor()
    query = "SELECT COUNT(DISTINCT (videoId)) FROM dictionary"
    cursor.execute(query)
    recount = cursor.fetchall()[0][0]-1
    cursor.close()
    return recount
