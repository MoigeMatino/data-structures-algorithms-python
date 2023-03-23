def intersection(a,b):
    my_set=set(a)
    return [element for element in b if element in my_set]

"""
This approach uses the set pass
Again, using a set is more efficient because it has O(1)
lookup time

n = length of array a, m = length of array b
Time: O(n+m)
Space: O(n)
"""