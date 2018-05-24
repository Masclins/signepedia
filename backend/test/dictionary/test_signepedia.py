import unittest
from src.dictionary import signepedia
from src import db

class TestSignepedia(unittest.TestCase):

    ###################
    # Tests get_entry #
    ###################

    # Checks all entries are returned as they should.
    # We don't test more synonyms nor corrections to avoid slowing the tests.
    def test_get_entry(self):
        words = ("Màster", "departament d'apòstrofs", "Roig", "Bermell", "INSTITUT")
        entries = (
                dict(word="màster", videoId="videos/màster.mp4", author="Tània"),
                dict(word="Departament d'apòstrofs", videoId="url_per_putejar", author="cabró", alternatives=["'", "ê", "é", "è"]),
                dict(word="Roig", synonyms=["vermell"]),
                dict(word="Bermell", correction="Vermell"),
                dict(word="institut", videoId="url_repetida", author="escriptor", alternatives=["col·legi", "escola"], synonyms=["estudi"]))

        cnx = db.connect()
        for word, entry in zip(words, entries):
            self.assertEqual(signepedia.get_entry(word, cnx), entry)
        cnx.close()

if __name__ == '__main__':
    unittest.main()
