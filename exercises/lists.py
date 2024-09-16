# Exercise 1: Reverse a list in place.
def reverse_list(lst):
    lst.sort(reverse = True)
    return lst
    pass

# Exercise 2: Find all unique elements in a list.
def find_unique_elements(lst):
    myset = set()
    for i in lst:
        myset.add(i)
    return list(myset)
    pass

# Exercise 3: Rotate a list by n positions.
def rotate_list(lst, n):
    for i in range(n):
        x = lst[0]
        lst.append(x)
        lst.pop(0)
    return lst
    pass

# Exercise 4: Flatten a list of lists.
def flatten_list(lst_of_lsts):
    flatten_result = list()
    for i in lst_of_lsts:
        for j in i:
            flatten_result.append(j)
    return flatten_result
    pass

# Exercise 5: Remove duplicates from a list.
def remove_duplicates(lst):
    myset = set()
    for i in lst:
        myset.add(i)
    return list(myset)
    pass
