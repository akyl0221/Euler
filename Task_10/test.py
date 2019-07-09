from .task import summ_primes
import unittest


class Test(unittest.TestCase):

    def test_is_int(self):
        self.assertEqual(summ_primes(1.1), 'Number must be Integer!')

    def test_positive_number(self):
        self.assertEqual(summ_primes(1), 'Number must be greater than 1')
