from .task import largest_product
import unittest


class Test(unittest.TestCase):

    def test_is_int(self):
        self.assertEqual(largest_product(1.1), 'Number must be Integer!')

    def test_positive_number(self):
        self.assertEqual(largest_product(-1), 'Number must be greater 1')