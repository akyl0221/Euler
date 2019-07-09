from .task import fibonacci_sum
import unittest

class Test(unittest.TestCase):

    def test_is_int(self):
        self.assertEqual(fibonacci_sum(1.1), 'Number must be Integer!')

    def test_positive_number(self):
        self.assertEqual(fibonacci_sum(-1), 'Number must be positive')
