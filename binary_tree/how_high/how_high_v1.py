def how_high(node):
    if node is None:
        return -1
    
    stack = [node]
    level =-1 #starting at -1 so that we can start counting the legitimate height from the children of the root
    while stack:
        
        for x in stack:
            if x.right:
                stack.append(x.right)
            if x.left:
                stack.append(x.left)
            stack.remove(x)
        level += 1
    return level

"""
DFS iterative approach
n - number of nodes
Time: O(n^2)
Space: O(n)
"""