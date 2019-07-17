from .task import max_prod_arr
import unittest


class Test(unittest.TestCase):

    def test_max_prod_count(self):
        self.assertEqual(max_prod_arr(), 70600674)
