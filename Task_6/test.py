from .task import difference_sqare_summ
import unittest


class Test(unittest.TestCase):

    def test_is_int(self):
        self.assertEqual(difference_sqare_summ(2.1), 'Number must be Integer!')

    def test_positive_number(self):
        self.assertEqual(difference_sqare_summ(1), 'Number must be greater 1')
