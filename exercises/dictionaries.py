# Exercise 1: Create a dictionary from two lists (keys and values).
def create_dict(keys, values):
    thisDict = {}
    for i, j in zip(keys, values):
        thisDict[i] = j
    return thisDict
    pass


# Exercise 2: Merge two dictionaries.
def merge_dicts(dict1, dict2):
    result = {**dict1, **dict2}
    return result
    pass

# Exercise 3: Find the key of the maximum value in a dictionary.
def max_value_key(d):
    sorted_result = list(d.keys())
    sorted_result.sort(reverse = True)
    return sorted_result[0]   
    pass

# Exercise 4: Sort a dictionary by values.
def sort_dict_by_value(d):
    sorted_result = list(d.keys())
    sorted_result.sort()
    result = {}
    for i in sorted_result:
        result.update({i: d[i]})
    return result
    pass

# Exercise 5: Count the occurrences of elements in a list using a dictionary.
def count_elements(lst):
    result = {}
    for i in lst:
        if i in result.keys():
            result[i] += 1
        else:
            result.update({i:1})
    return result
    pass
