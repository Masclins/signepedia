import unittest
import datetime
import users
import db

class TestUsers(unittest.TestCase):

    ##################
    # Tests new_user #
    ##################

    # Checks we add new user.
    def test_new_user(self):
        cnx = db.connect()
        cursor = cnx.cursor(dictionary=True)

        cursor.execute("DELETE FROM users WHERE name='Bruno'")
        newUser = dict(
                name="Bruno",
                email="bruno@mit.com",
                password="1234",
                birthday="1990-01-01")
        users.new_user(newUser, cursor)
        cursor.execute("SELECT * FROM users WHERE name='Bruno'")
        insertedEntry = cursor.fetchall()[0]
        self.assertEqual(insertedEntry["name"], "Bruno")
        self.assertEqual(insertedEntry["email"], "bruno@mit.com")
        self.assertEqual(insertedEntry["password"], "1234")
        self.assertEqual(insertedEntry["birthday"], datetime.datetime(1990, 1, 1))
        self.assertEqual(insertedEntry["mod_level"], 0)

    # Checks errors for already registered name and email.
        self.assertEqual(
            users.new_user(dict(name="Bruno", email="mail@diferent.com"), cursor),
            "name")
        self.assertEqual(
            users.new_user(dict(name="no-Bruno", email="bruno@mit.com"), cursor),
            "email")

        cursor.close()
        cnx.close()

if __name__ == '__main__':
    unittest.main()
