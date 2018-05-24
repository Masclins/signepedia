import unittest
from src.dictionary import synonyms
from src import db


class TestSynonyms(unittest.TestCase):

    ##########################
    # Tests request_synonyms #
    ##########################

    # Checks synonyms are gotten without repetitions.
    def test_get_sinonims(self):
        self.assertEqual(
                synonyms.request_synonyms("prova"),
                ["assaig", "experiment", "experimentació", "intent", "provatura", "temptativa", "tempteig", "test", "demostració", "examen"])


    ######################
    # Tests get_synonyms #
    ######################

    # Checks only registered synonyms are returned.
    def test_get_synonyms(self):
        cnx = db.connect()
        self.assertEqual(
                synonyms.get_synonyms("escola", cnx),
                ["col·legi", "estudi", "institut"])
        self.assertEqual(
                synonyms.get_synonyms("llamp", cnx),
                None)
        cnx.close()

if __name__ == '__main__':
    unittest.main()
