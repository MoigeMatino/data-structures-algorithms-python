def intersection(a,b):
    intersection=[]
    for element in b:
        if element in a:
            intersection.append(element)
    
    return intersection

"""

n = length of array a, m = length of array b
Time: O(n*m)
Space: O(min(n,m))


"""