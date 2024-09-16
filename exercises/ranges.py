# Exercise 1: Create a list of numbers using range().
def create_range(start, end, step=1):
    list = []
    for i in range(start, end, step):
        list.append(i)
    return list
    pass

# Exercise 2: Sum all elements in a range.
def sum_range(start, end):
    result = 0
    for i in range(start, end):
        result += i
    return result
    pass

# Exercise 3: Check if a number is within a range.
def in_range(n, start, end):
    for i in range(start, end):
        if n == i:
            return True
    return False
    pass

# Exercise 4: Create a list of even numbers using range().
def even_numbers(start, end):
    lst = []
    for i in range(start,end):
        print(i)
        if i % 2 == 0:
            lst.append(i)
    print(lst)
    return lst
    pass

# Exercise 5: Iterate over a range in reverse.
def reverse_range(start, end):
    lst = []
    for i in range(end - 1, start - 1, -1):
        lst.append(i)
    return lst
    pass
