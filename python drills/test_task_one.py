import unittest
import task_one


class test_for_length_of_list(unittest.TestCase):
    def test_get_length_of_list(self):
        list1 = [10, 20, 30, 40, 50, 50, 60, 70, 80, 90]
        self.assertEqual(10, task_one.get_list_length(list1))


    def test_get_sum_of_even_index_elements(self):
        list1 = [10, 20, 30, 40, 50, 50, 60, 70, 80, 90]
        self.assertEqual(270, task_one.get_list_sum_of_even_elements(list1))

    def test_get_sum_of_odd_index_elements(self):
        list1 = [10, 20, 30, 40, 50, 50, 60, 70, 80, 90]
        self.assertEqual(230, task_one.get_list_sum_of_odd_index_elements(list1))

    def test_for_product_of_third_position_elements(self):
        list1 = [10, 20, 30, 40, 50, 50, 60, 70, 80, 90]
        self.assertEqual(72000000, task_one.multiply_third_elements(list1))

    def test_for_sum_of_all_elements_in_list(self):
        list1 = [10, 20, 30, 40, 50, 50, 60, 70, 80, 90]
        self.assertEqual(500, task_one.get_list_total(list1))

    def test_for_maximum_in_list(self):
        list1 = [10, 20, 30, 40, 50, 50, 60, 70, 80, 90]
        self.assertEqual(90, task_one.get_highest_in_list(list1))

    def test_for_minimum_in_list(self):
        list1 = [10, 20, 30, 40, 50, 50, 60, 70, 80, 90]
        self.assertEqual(10, task_one.get_lowest_in_list(list1))


    def test_for_length_of_strings_in_list(self):
        list1 = ['obo', 'days', 'eye', 'aa', 'bags']
        self.assertListEqual(['obo', 'eye', 'aa'], task_one.get_common_strings(list1))