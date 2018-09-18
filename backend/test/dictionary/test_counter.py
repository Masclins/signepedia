import unittest
from dictionary import counter
import db


class TestCounter(unittest.TestCase):

    #####################
    # Tests get_nVideos #
    #####################

    # Checks it counts correctly.
    def test_get_nVideos(self):
        cnx = db.connect()
        cursor = cnx.cursor(dictionary=True)

        self.assertEqual(counter.get_nVideos(cursor), 3)

        cursor.close()
        cnx.close()

if __name__ == '__main__':
    unittest.main()
