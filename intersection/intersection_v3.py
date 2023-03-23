def intersection(a,b):
    intersection=[]
    for element in a:
        if element in b:
            intersection.append(element)
    
    return intersection

"""

n = length of array a, m = length of array b
Time: O(n*m)
Space: O(min(n,m))


"""