import unittest
import datetime
from dictionary import main
import db

class TestMain(unittest.TestCase):

    ###################
    # Tests get_entry #
    ###################

    # Checks all entries are returned as they should.
    # We don't test more synonyms nor corrections to avoid slowing the tests.
    def test_get_result(self):
        self.maxDiff = None
        cnx = db.connect()
        cursor = cnx.cursor(dictionary=True)
        words = ("roig", "bermell", "TROLL'd")
        answers = (
            dict(
                nVideos=3,
                word="roig",
                synonyms=["vermell"]),
            dict(
                nVideos=3,
                word="bermell",
                correction="vermell"),
            dict(
                nVideos=3,
                word="TROLL'd",
                entries=[
                    dict(
                        id=4,
                        word="troll'd",
                        hex="74726F6C6C2764",
                        video="oavMtUWDBTM",
                        id_user=2,
                        comment=None,
                        date_added=datetime.datetime(2009, 11, 26),
                        date_updated=datetime.datetime(2009, 11, 26),
                        likes=1,
                        dislikes=2,
                        valid=0),
                    dict(
                        id=2,
                        word="troll'd",
                        hex="74726F6C6C2764",
                        video="dQw4w9WgXcQ",
                        id_user=1,
                        comment="You'd been Rickroll'd!",
                        date_added=datetime.datetime(2001, 1, 1),
                        date_updated=datetime.datetime(2001, 1, 1),
                        likes=0,
                        dislikes=100,
                        valid=1)]))

        for word, answer in zip(words, answers):
            self.assertEqual(main.get_result(word, cursor), answer)

        cursor.close()
        cnx.close()

    #########################
    # Tests get_result_user #
    #########################

    # Checks we get the vote as casted.
    def test_get_result_user(self):
        cnx = db.connect()
        cursor = cnx.cursor(dictionary=True)

        cursor.execute("INSERT INTO votes VALUES (4, 1, 'like', '2000-01-01')")
        entries = main.get_result_user("troll'd", 1, cursor)["entries"]
        self.assertEqual(entries[0]["vote"], "like")
        self.assertEqual(entries[1]["vote"], "owner")

        self.assertFalse("vote" in main.get_result_user("troll'd", 3, cursor)["entries"][0])

        cursor.close()
        cnx.close()

if __name__ == '__main__':
    unittest.main()
