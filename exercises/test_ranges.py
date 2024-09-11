import unittest
from ranges import *

class TestRanges(unittest.TestCase):

    def test_create_range(self):
        self.assertEqual(create_range(1, 5), [1, 2, 3, 4])

    def test_sum_range(self):
        self.assertEqual(sum_range(1, 5), 10)

    def test_in_range(self):
        self.assertTrue(in_range(3, 1, 5))

    def test_even_numbers(self):
        self.assertEqual(even_numbers(2, 10), [2, 4, 6, 8])

    def test_reverse_range(self):
        self.assertEqual(reverse_range(1, 5), [4, 3, 2, 1])

if __name__ == '__main__':
    unittest.main()
