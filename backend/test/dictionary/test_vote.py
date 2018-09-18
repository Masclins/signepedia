import unittest
from dictionary import vote
import db

class TestVote(unittest.TestCase):
    #############
    #Tests vote #
    #############

    # Checks votes are properly registered.
    def test_vote(self):
        cnx = db.connect()
        cursor = cnx.cursor(dictionary=True)

        cursor.execute("UPDATE dictionary SET likes=0, dislikes=100 WHERE id=2")
        cursor.execute("DELETE FROM votes")
        vote.vote(2, 99, "like", cursor)
        cursor.execute("SELECT likes FROM dictionary WHERE id=2")
        self.assertEqual(cursor.fetchall()[0]["likes"], 1)
        vote.vote(2, 42, "dislike", cursor)
        cursor.execute("SELECT dislikes FROM dictionary WHERE id=2")
        self.assertEqual(cursor.fetchall()[0]["dislikes"], 101)

        cursor.execute("SELECT * FROM votes")
        rows = cursor.fetchall()
        entryIds = (2, 2)
        userIds = (99, 42)
        voteTypes = ("like", "dislike")
        for row, entryId, userId, voteType in zip(rows, entryIds, userIds, voteTypes):
            self.assertEqual(row["id_entry"], entryId)
            self.assertEqual(row["id_user"], userId)
            self.assertEqual(row["vote"], voteType)

        self.assertFalse(vote.canVote(2, 42, cursor))
        self.assertFalse(vote.canVote(1, 1, cursor))

        cursor.close()
        cnx.close()

if __name__ == '__main__':
    unittest.main()
