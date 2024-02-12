import unittest
from drill import set_element_removal

class MySetTest(unittest.TestCase):
    def test_remove_existing_element_from_set_returns_element(self):
        my_set = {2, 6, 4, 3}
        number = 6
        self.assertEqual(6, set_element_removal.remove_item(my_set, number))  # add assertion here


    def test_remove_non_existing_element_from_set_none_returns(self):
        my_set = {2, 6, 4, 3}
        number = 8
        self.assertEqual(None, set_element_removal.remove_item(my_set, number))  # add assertion here
