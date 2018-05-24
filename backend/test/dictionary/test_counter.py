import unittest
from src.dictionary import counter
from src import db


class TestCounter(unittest.TestCase):

    ##################
    # Tests videoIds #
    ##################

    # Checks it counts correctly.
    def test_urls(self):

        cnx = db.connect()
        self.assertEqual(counter.videoIds(cnx), 8)
        cnx.close()

if __name__ == '__main__':
    unittest.main()
