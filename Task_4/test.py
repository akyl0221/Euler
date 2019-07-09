from .task import palindrome
import unittest


class Test(unittest.TestCase):

    def test_is_int(self):
        self.assertEqual(palindrome(2.1), 'Number must be Integer!')

    def test_positive_number(self):
        self.assertEqual(palindrome(-1), 'Number must be greater 1')

    def test_answer(self):
        self.assertTrue(palindrome(3), 9009)