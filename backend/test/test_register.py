import unittest
from src import register
from src import db

class TestRegister(unittest.TestCase):

    #########################
    # Tests register_search #
    #########################

    # Checks that creates and increases when required.
    def test_register_search(self):
        cnx = db.connect()

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("DELETE FROM views WHERE word='never_is'")
        register.register_search("never_is", cnx)
        cursor.execute("SELECT word, num FROM views WHERE word='never_is'")
        self.assertEqual(cursor.fetchall()[0], dict(word="never_is", num=1))
        query = "SELECT num FROM views WHERE word='always_is'"
        cursor.execute(query)
        initial = cursor.fetchall()[0]["num"]
        register.register_search("always_is", cnx)
        cursor.execute(query)
        self.assertEqual(cursor.fetchall()[0]["num"], initial + 1)

        cursor.close()
        cnx.close()

if __name__ == '__main__':
    unittest.main()
