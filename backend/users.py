import datetime

# Adds a new user to database
def new_user(newUser, cursor):
    query = "SELECT * FROM users WHERE email LIKE %s LIMIT 1"
    cursor.execute(query, (newUser["email"],))
    cursor.fetchall()
    if cursor.rowcount != 0:
        return "email"
    query = "SELECT * FROM users WHERE name LIKE %s LIMIT 1"
    cursor.execute(query, (newUser["name"],))
    cursor.fetchall()
    if cursor.rowcount != 0:
        return "name"

    query = "INSERT INTO users VALUES (NULL, %s, %s, %s, %s, %s, 0)"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    cursor.execute(query, (
        newUser["name"],
        newUser["email"],
        newUser["password"],
        now,
        now))
    return "done"
