import unittest
from dictionary import search
import db

class TestSearcher(unittest.TestCase):

    ###################
    # Tests got_entry #
    ###################

    # Checks it gets it correctly
    def test_got_entry(self):
        cnx = db.connect()
        cursor = cnx.cursor(dictionary=True)

        self.assertTrue(search.got_entry("TroLoLo", cursor))
        self.assertTrue(search.got_entry("troll'd", cursor))
        self.assertFalse(search.got_entry("foo", cursor))
        self.assertFalse(search.got_entry("bar", cursor))

        cursor.close()
        cnx.close()

    #####################
    # Tests get_entries #
    #####################

    # Checks it gets the entries correctly.
    def test_get_entries(self):
        cnx = db.connect()
        cursor = cnx.cursor(dictionary=True)

        searchedWords = ("rickroll", "troll'd", "TROLOLO", "Shupe")
        words = ("Rickroll", "troll'd", "Trololo", None)
        vVideos = (["dQw4w9WgXcQ"], ["oavMtUWDBTM", "dQw4w9WgXcQ"], ["oavMtUWDBTM"], [])
        vIdUsers = ([1], [2, 1], [2], [])
        vComments = ([None], [None, "You'd been Rickroll'd!"], [None], [])

        for searchedWord, word, videos, idUsers, comments in zip(searchedWords, words, vVideos, vIdUsers, vComments):
            entries = search.get_entries(searchedWord, cursor)
            for entry, video, idUser, comment in zip(entries, videos, idUsers, comments):
                self.assertEqual(entry["word"], word)
                self.assertEqual(entry["video"], video)
                self.assertEqual(entry["id_user"], idUser)
                self.assertEqual(entry["comment"], comment)

        cursor.close()
        cnx.close()

if __name__ == '__main__':
    unittest.main()
