import unittest
import register
import db

class TestRegister(unittest.TestCase):

    ##################
    # Tests searches #
    ##################

    # Checks that creates and increases when required.
    def test_searches(self):
        cnx = db.connect()
        cursor = cnx.cursor(dictionary=True)

        cursor.execute("DELETE FROM searches WHERE word='BAR'")
        register.searches("bar", cursor)
        cursor.execute("SELECT * FROM searches WHERE hex='626172'")
        self.assertEqual(
                cursor.fetchall()[0],
                dict(word="bar",
                    hex="626172",
                    number=1,
                    ignored=0))
        register.searches("baR", cursor)
        cursor.execute("SELECT * FROM searches WHERE hex='626172'")
        self.assertEqual(
                cursor.fetchall()[0],
                dict(word="bar",
                    hex="626172",
                    number=2,
                    ignored=0))

        cursor.close()
        cnx.close()

    ################
    # Tests ignore #
    ################

    # Checks it is really set to ignore
    def test_ignore(self):
        cnx = db.connect()
        cursor = cnx.cursor(dictionary=True)

        cursor.execute("DELETE FROM searches WHERE word='zet'")
        register.searches("zet", cursor)
        register.ignore("ZET", cursor)
        cursor.execute("SELECT * FROM searches WHERE hex='7A6574'")
        self.assertEqual(cursor.fetchall()[0]["ignored"], 1)

        cursor.close()
        cnx.close()

if __name__ == '__main__':
    unittest.main()
