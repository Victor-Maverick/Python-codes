import unittest
from drill import set_sum


class MySetTest(unittest.TestCase):
    def test_sum_of_of_a_set(self):
        numbers = {1, 2, 3, 4, 5}
        self.assertEqual(15, set_sum.sum_collection(numbers))  # add assertion here


