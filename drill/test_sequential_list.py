import unittest
from drill import sequential_list


class SequentialListTest(unittest.TestCase):
    def test_list_is_constructed(self):
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(my_list, sequential_list.construct_list())  # add assertion here


    def test_duplicated_list(self):
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        dup_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(dup_list, sequential_list.duplicate_list(my_list))

    def test_duplicated_list(self):
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        dup_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(my_list, sequential_list.remove_duplicate_elements_in_list(dup_list))