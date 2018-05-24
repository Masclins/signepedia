import unittest
from src import unvalidated
from src import db

class TestUnvalidated(unittest.TestCase):

    ################
    # Tests insert #
    ################

    # Checks we add new unvalidated entries.
    # Comprovem que afegeix noves entrades.
    def test_insert(self):
        cnx = db.connect()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("DELETE FROM unvalidated WHERE word='Brunada'")
        newEntry = dict(
                word="Brunada",
                videoId="8rUn0",
                author="Bruno")
        unvalidated.insert(newEntry, cnx)
        cursor.execute("SELECT * FROM unvalidated WHERE word='Brunada'")
        insertedEntry = cursor.fetchall()[0]
        self.assertEqual(insertedEntry["word"], "Brunada")
        self.assertEqual(insertedEntry["videoId"], "8rUn0")
        self.assertEqual(insertedEntry["author"], "Bruno")
        self.assertTrue(insertedEntry["id"] > 0)
        cursor.close()
        cnx.close()

    ##################
    # Tests validate #
    ##################

    # Checks an entry is correctly validated.
    def test_validate(self):
        cnx = db.connect()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("INSERT INTO unvalidated VALUES ('validada', '10_10', 'mr. Smith', 1)")
        validEntry = dict(
                id=1,
                word="VALIDADA!",
                author="Mr. Smith",
                alternatives="aquestaésbona")
        unvalidated.validate(validEntry, cnx)
        cursor.execute("SELECT * FROM dictionary WHERE hex='76616C696461646121'")
        self.assertEqual(
                cursor.fetchall()[0],
                dict(
                    word="VALIDADA!",
                    videoId="10_10",
                    author="Mr. Smith",
                    alternatives="aquestaésbona",
                    hex="76616C696461646121"))
        cursor.execute("SELECT COUNT(word) FROM unvalidated WHERE id=1")
        self.assertEqual(cursor.fetchall()[0]["COUNT(word)"], 0)
        cursor.execute("DELETE FROM dictionary WHERE hex='76616C696461646121'")
        cursor.close()
        cnx.commit()
        cnx.close()

    #########################
    # Tests get_unvalidated #
    #########################

    # Checks we are getting the first unvalidated entry.
    def test_unvalidated(self):
        cnx = db.connect()
        self.assertEqual(
                unvalidated.get_unvalidated(cnx),
                dict(
                    word="a",
                    videoId="b",
                    author="c",
                    id=2))
        cnx.close()

if __name__ == '__main__':
    unittest.main()
