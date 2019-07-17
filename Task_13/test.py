from .task import find_summ
import unittest


class Test(unittest.TestCase):

    def test_find_summ(self):
        self.assertEqual(find_summ(), 5537376230390876637302048746832985971773659831892672)
