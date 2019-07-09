import unittest
from . import task


class Task1Test(unittest.TestCase):
    def setUp(self) -> None:
        self.summ = task.summ_calculate()

    def test_summ(self):
        self.assertEqual(self.summ, 233168)
