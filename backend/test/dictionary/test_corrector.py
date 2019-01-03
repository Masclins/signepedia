import unittest
from dictionary import corrector
import db

class TestCorrector(unittest.TestCase):

    #############################
    # Tests request_corrections #
    #############################

    # Checks the requests to LanguageTool.
    def test_request_corrections(self):
        corrections = corrector.request_corrections("clase")
        self.assertEqual(corrections[0], "classe")
        self.assertEqual(corrections[1], "casa")
        self.assertEqual(corrector.request_corrections("jksdfjfqp"), None)

    ########################
    # Tests get_correction #
    ########################

    # Checks the entry is returned with the proposed correction.
    def test_get_correction(self):
        cnx = db.connect()
        cursor = cnx.cursor(dictionary=True)

        self.assertEqual(corrector.get_correction("bermell", cursor), "vermell")
        self.assertEqual(corrector.get_correction("miñisteri", cursor), None)

        cursor.close()
        cnx.close()

if __name__ == '__main__':
    unittest.main()
