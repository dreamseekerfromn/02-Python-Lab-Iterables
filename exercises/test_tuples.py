import unittest
from tuples import *

class TestTuples(unittest.TestCase):

    def test_access_tuple_element(self):
        self.assertEqual(access_tuple_element((1, 2, 3), 1), 2)

    def test_tuple_to_list(self):
        self.assertEqual(tuple_to_list((1, 2, 3)), [1, 2, 3])

    def test_list_to_tuple(self):
        self.assertEqual(list_to_tuple([1, 2, 3]), (1, 2, 3))

    def test_find_tuple_index(self):
        self.assertEqual(find_tuple_index((1, 2, 3), 2), 1)

    def test_concatenate_tuples(self):
        self.assertEqual(concatenate_tuples((1, 2), (3, 4)), (1, 2, 3, 4))

if __name__ == '__main__':
    unittest.main()
