from .task import smallest_positive
import unittest


class Test(unittest.TestCase):

    def test_is_int(self):
        self.assertEqual(smallest_positive(2.1), 'Number must be Integer!')

    def test_positive_number(self):
        self.assertEqual(smallest_positive(8), 'Number must be greater 9')
