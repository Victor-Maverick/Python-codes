from drill import set_intersection

import unittest



class MySetTest(unittest.TestCase):
    def test_to_combine_two_sets(self):
        my_set = {1, 2, 3, 4}
        new_set = {4, 5, 3, 6}
        intersect = {3, 4}
        self.assertSetEqual(intersect, set_intersection.find_intersection(my_set, new_set))


