def how_high(node):
    if node is None:
        return -1
    distance = 0
    max = 0
    stack = [(node,distance)]
        
    while stack:
        x, distance = stack.pop()
        
        if x.left:
            stack.append((x.left, distance+1)) 
        if x.right:
            stack.append((x.right, distance+1))
        
        if distance > max:
            max = distance
        
        
    return max

"""

n = number of nodes
Time: O(n)
Space: O(n)

"""