import unittest
import auth
import run


class TestValidate(unittest.TestCase):
    """
    Verification of the user email
    input values and types
    """
    def test_validate_email(self):
        self.assertTrue(auth.validate_user_email('testemail@gmail.com'), True)

    def test_validate_wrong_email(self):
        self.assertEqual(auth.validate_user_email('465432'), None)

    def test_validate_play_game(self):
        self.assertTrue(run.play_game('John', 'word'), True)

    def test_validate_wrong_play_game(self):
        self.assertTrue(run.play_game(1, ['test', 'word']), False)
