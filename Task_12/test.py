from .task import find_triangle
import unittest


class Test(unittest.TestCase):

    def test_is_int(self):
        self.assertEqual(find_triangle(1.1), 'Number must be Integer!')

    def test_positive_number(self):
        self.assertEqual(find_triangle(0), 'Number must be greater than 1')
