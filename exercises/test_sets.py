import unittest
from sets import *

class TestSets(unittest.TestCase):

    def test_create_set(self):
        self.assertEqual(create_set([1, 2, 2, 3]), {1, 2, 3})

    def test_union_sets(self):
        self.assertEqual(union_sets({1, 2}, {2, 3}), {1, 2, 3})

    def test_intersection_sets(self):
        self.assertEqual(intersection_sets({1, 2}, {2, 3}), {2})

    def test_is_subset(self):
        self.assertTrue(is_subset({1, 2}, {1, 2, 3}))

    def test_symmetric_difference_sets(self):
        self.assertEqual(symmetric_difference_sets({1, 2}, {2, 3}), {1, 3})

if __name__ == '__main__':
    unittest.main()
