import unittest
from dictionary import alter
import db

class TestAlter(unittest.TestCase):

    ################
    # Tests insert #
    ################

    # Checks we add new unvalidated entries.
    def test_insert(self):
        cnx = db.connect()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("DELETE FROM dictionary WHERE word='foo'")
        newEntry = dict(
                word="foo",
                video="F0o",
                idUser=99,
                comment=None)

        alter.insert(newEntry, cursor)
        cursor.execute("SELECT * FROM dictionary WHERE word='foo'")
        insertedEntry = cursor.fetchall()[0]
        self.assertTrue(insertedEntry["id"] > 0)
        self.assertEqual(insertedEntry["word"], "foo")
        self.assertEqual(insertedEntry["hex"], "666F6F")
        self.assertEqual(insertedEntry["video"], "F0o")
        self.assertEqual(insertedEntry["id_user"], 99)
        self.assertEqual(insertedEntry["comment"], None)
        self.assertEqual(insertedEntry["likes"], 0)
        self.assertEqual(insertedEntry["dislikes"], 0)
        self.assertEqual(insertedEntry["valid"], 0)

        cursor.close()
        cnx.close()

    #########################
    # Tests get_unvalidated #
    #########################

    # Checks we are getting all the unvalidated entries.
    def test_unvalidated(self):
        cnx = db.connect()
        cursor = cnx.cursor(dictionary=True)

        self.assertEqual(
                len(alter.get_unvalidated(cursor)),
                3)

        cursor.close()
        cnx.close()

    ####################
    # Tests edit_entry #
    ####################

    # Checks editions are properly done.
    def test_edit_entry(self):
        cnx = db.connect()
        cursor = cnx.cursor(dictionary=True)

        edits = dict(word="TROOLL!", comment="Now it has a comment", video="XXX")
        alter.edit_entry(3, edits, cursor)
        cursor.execute("SELECT word, comment, video FROM dictionary WHERE id=2")
        self.assertTrue(cursor.fetchall()[0], edits)

        cursor.close()
        cnx.close()

    ######################
    # Tests delete_entry #
    ######################

    # Checks a test is deleted and moved to graveyard.
    def test_delete_entry(self):
        cnx = db.connect()
        cursor = cnx.cursor(dictionary=True)

        cursor.execute("INSERT INTO dictionary VALUES (9001, \"dead\", Hex(\"dead\"), \"XXX\", 0, NULL, \"2012-01-01\", \"2012-01-01\", 1, 2, 0)")
        alter.delete_entry(9001, cursor)
        cursor.execute("SELECT * FROM dictionary_graveyard WHERE id=9001")
        deadEntry = cursor.fetchall()[0]
        self.assertEqual(deadEntry["word"], "dead")
        cursor.execute("DELETE FROM dictionary_graveyard WHERE id=9001")
        cursor.execute("SELECT * FROM dictionary WHERE id=9001")
        cursor.fetchall()
        self.assertEqual(cursor.rowcount, 0)

        cursor.close()
        cnx.close()

if __name__ == '__main__':
    unittest.main()
