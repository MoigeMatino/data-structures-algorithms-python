def intersection(a,b):
    intersection=[]
    my_set={element for element in a}
    for element in b:
        if element in my_set:
            intersection.append(element)
    return intersection

"""
n = length of array a, m = length of array b
Time:O(n+m)
Space: O(n)

A set is used because it is more efficient for lookup
with a O(1)

"""