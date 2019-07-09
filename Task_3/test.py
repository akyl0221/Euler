from .task import prime_factors
import unittest

class Test(unittest.TestCase):

    def test_is_int(self):
        self.assertEqual(prime_factors(1.1), 'Number must be Integer!')

    def test_positive_number(self):
        self.assertEqual(prime_factors(1), 'Number must be greater than 1')
