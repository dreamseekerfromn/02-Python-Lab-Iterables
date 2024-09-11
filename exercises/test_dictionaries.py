import unittest
from dictionaries import create_dict, merge_dicts, max_value_key, sort_dict_by_value, count_elements

class TestDictionaries(unittest.TestCase):

    def test_create_dict(self):
        self.assertEqual(create_dict(['a', 'b'], [1, 2]), {'a': 1, 'b': 2})

    def test_merge_dicts(self):
        self.assertEqual(merge_dicts({'a': 1}, {'b': 2}), {'a': 1, 'b': 2})

    def test_max_value_key(self):
        self.assertEqual(max_value_key({'a': 1, 'b': 2}), 'b')

    def test_sort_dict_by_value(self):
        self.assertEqual(sort_dict_by_value({'a': 3, 'b': 1}), {'b': 1, 'a': 3})

    def test_count_elements(self):
        self.assertEqual(count_elements([1, 2, 2, 3]), {1: 1, 2: 2, 3: 1})

if __name__ == '__main__':
    unittest.main()
