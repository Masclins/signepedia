import unittest
from dictionary import synonyms
import db


class TestSynonyms(unittest.TestCase):

    ##########################
    # Tests request_synonyms #
    ##########################

    # Checks synonyms are gotten without repetitions.
    def test_request_synonyms(self):
        self.assertEqual(
                synonyms.request_synonyms("vermell"),
                ["roig", "roja", "vermella"])

    # Checks errors are handled properly.
    def test_request_synonyms_error(self):
        self.assertEqual(synonyms.request_synonyms("&2Troll"), [])

        cnx = db.connect()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM errors WHERE function='request_synonyms' AND variables='&2Troll'")
        cursor.fetchall()
        self.assertTrue(cursor.rowcount > 0)

        cursor.execute("DELETE FROM errors WHERE function='request_synonyms' AND variables='&2Troll'")
        cnx.commit()
        cursor.close()
        cnx.close()

    ######################
    # Tests get_synonyms #
    ######################

    # Checks only registered synonyms are returned.
    def test_get_synonyms(self):
        cnx = db.connect()
        cursor = cnx.cursor(dictionary=True)

        self.assertEqual(
                synonyms.get_synonyms("roig", cursor),
                ["vermell"])
        self.assertEqual(
                synonyms.get_synonyms("llamp", cursor),
                None)

        cursor.close()
        cnx.close()

if __name__ == '__main__':
    unittest.main()
