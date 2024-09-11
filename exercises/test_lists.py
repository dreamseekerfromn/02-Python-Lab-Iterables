import unittest
from lists import *

class TestLists(unittest.TestCase):

    def test_reverse_list(self):
        self.assertEqual(reverse_list([1, 2, 3]), [3, 2, 1])

    def test_find_unique_elements(self):
        self.assertEqual(find_unique_elements([1, 2, 2, 3]), [1, 2, 3])

    def test_rotate_list(self):
        self.assertEqual(rotate_list([1, 2, 3, 4], 2), [3, 4, 1, 2])

    def test_flatten_list(self):
        self.assertEqual(flatten_list([[1, 2], [3, 4]]), [1, 2, 3, 4])

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3]), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
