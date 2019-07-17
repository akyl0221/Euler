from .task import rec_path
import unittest


class Test(unittest.TestCase):

    def test_rec_path(self):
        self.assertEqual(rec_path([20, 20]), 6)