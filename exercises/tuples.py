# Exercise 1: Access elements from a tuple.
def access_tuple_element(tpl, index):
    return tpl[index]
    pass

# Exercise 2: Convert a tuple to a list and vice versa.
def tuple_to_list(tpl):
    return list(tpl)
    pass

def list_to_tuple(lst):
    return tuple(lst)
    pass

# Exercise 3: Find the index of an element in a tuple.
def find_tuple_index(tpl, element):
    for i in range(len(tpl)):
        if tpl[i] == element:
            return i
    pass

# Exercise 4: Unpack a tuple into variables.
def unpack_tuple(tpl):
    pass

# Exercise 5: Concatenate two tuples.
def concatenate_tuples(tpl1, tpl2):
    return tpl1 + tpl2
    pass
