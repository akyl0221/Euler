from .task import collatz_sequence
import unittest


class Test(unittest.TestCase):

    def test_collatz_sequence(self):
        self.assertEqual(collatz_sequence(), 837799)
