import unittest
from src.dictionary import corrector
from src import db

class TestCorrector(unittest.TestCase):

    #############################
    # Tests request_corrections #
    #############################

    # Checks the requests to LanguageTool.
    def test_request_corrections(self):
        corrections = corrector.request_corrections("clase")
        self.assertEqual(corrections[0], "classe")
        self.assertEqual(corrections[1], "casa")

    def test_fail(self):
        self.assertEqual(corrector.request_corrections("jksdfjfqp"), None)
        self.assertEqual(corrector.request_corrections("sant jordi"), None)

    ########################
    # Tests get_correction #
    ########################

    # Checks the entry is returned with the proposed correction.
    def test_get_correction(self):
        cnx = db.connect()
        self.assertEqual(corrector.get_correction("master", cnx), {"word": "master", "correction": "màster"})
        self.assertEqual(corrector.get_correction("miñisteri", cnx), {"word": "miñisteri"})
        cnx.close()

if __name__ == '__main__':
    unittest.main()
