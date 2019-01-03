# Rgisters the search of a word.
def searches(word, cursor):
    query = "INSERT INTO searches VALUES (LOWER(%s), Hex(LOWER(%s)), 1, 0) ON DUPLICATE KEY UPDATE number=number+1"
    cursor.execute(query, (word, word))

# Sets a register to be ignored (so no longer shown)
def ignore(word, cursor):
    query = "UPDATE searches SET ignored=1 WHERE hex=Hex(LOWER(%s))"
    cursor.execute(query, (word,))
