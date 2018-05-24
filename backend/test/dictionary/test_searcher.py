import unittest
from src.dictionary import searcher
from src import db

class TestSearcher(unittest.TestCase):

    ###################
    # Tests got_entry #
    ###################

    # Checks it gets it correctly
    def test_got_entry(self):
        cnx = db.connect()
        self.assertTrue(searcher.got_entry("col·legi", cnx))
        self.assertTrue(searcher.got_entry("dePARtament d'ApÒstrofs", cnx))
        self.assertFalse(searcher.got_entry("qkañ", cnx))
        self.assertFalse(searcher.got_entry("brunada", cnx))
        cnx.close()

    #####################
    # Tests clean_entry #
    #####################

    # Checks it's properly cleaned
    def test_clean_entry(self):
        self.assertEqual(
                searcher.clean_entry(dict(a="foo", b="", c="bar", alternatives="")),
                dict(a="foo", c="bar"))
        self.assertEqual(
                searcher.clean_entry(dict(word="Hola", alternatives="Hola què tal?|Bon dia|Hola i adéu")),
                dict(word="Hola", alternatives=["Hola què tal?", "Bon dia", "Hola i adéu"]))

    ###################
    # Tests get_entry #
    ###################

    # Checks an unregistered entry response.
    def test_get_entry_unregistered(self):
        cnx = db.connect()
        self.assertEqual(searcher.get_entry("bermell", cnx), None)
        self.assertEqual(searcher.get_entry("", cnx), None)
        self.assertEqual(searcher.get_entry("¿ ?", cnx), None)
        cnx.close()

    # Checks it gets the entry correctly.
    def test_get_entry(self):
        searchedWords = ("col·legi", "Institut", "tomàquet", "tomaquet", "barcelona")
        words = ("col·legi", "institut", "tomàquet", "tomaquet", "Barcelona")
        videoIds = ("url_del_col·legi", "url_repetida", "url_gran", "url_petita", "url_BCN")
        authors = ("autor", "escriptor", "gran", "petit", "alcalde")

        cnx = db.connect()
        for searchedWord, word, videoId, author in zip(searchedWords, words, videoIds, authors):
            entry = searcher.get_entry(searchedWord, cnx)
            self.assertEqual(entry["word"], word)
            self.assertFalse("correccio" in entry)
            self.assertEqual(entry["videoId"], videoId)
            self.assertEqual(entry["author"], author)
        cnx.close()

    def test_get_entry_alternatives(self):
        words = ("institut", "tomaquet")
        alternativess = (["col·legi", "escola"], ["tomàquet"])

        cnx = db.connect()
        for word, alternatives in zip(words, alternativess):
            self.assertEqual(
                    searcher.get_entry(word, cnx)["alternatives"],
                    alternatives)
        self.assertFalse("alternatives" in searcher.get_entry("màster", cnx))
        cnx.close()

if __name__ == '__main__':
    unittest.main()
