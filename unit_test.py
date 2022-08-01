"""
Unit tests
"""
import unittest
import auth
import run


class TestValidate(unittest.TestCase):
    """
    Verification of the user email
    input values and types
    """
    def test_validate_email(self):
        """
        Unit Test of validate user email function with incorrect values
        """
        self.assertTrue(auth.validate_user_email('testemail@gmail.com'), True)

    def test_validate_wrong_email(self):
        """
        Unit Test of validate user email function with incorrect values
        """
        self.assertEqual(auth.validate_user_email('465432'), None)

    def test_validate_play_game(self):
        """
        Unit Test of play game function with correct values
        """
        self.assertTrue(run.play_game('John', 'word'), True)

    def test_validate_wrong_play_game(self):
        """
        Unit Test of play game function with incorrect values
        """
        self.assertTrue(run.play_game(1, ['test', 'word']), False)


if __name__ == '__main__':
    unittest.main()
