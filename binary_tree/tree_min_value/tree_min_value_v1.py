from collections import deque

def tree_min_value(root):
    min = float("inf")
    queue = deque([root])
    
    while queue:
        current = queue.popleft()
        if current.val < min:
            min = current.val
        
        if current.left:
            queue.append(current.left)
        
        if current.right:
            queue.append(current.right)
        
    return min

"""
BFS iterative approach

n = number of nodes
Time: O(n)
Space: O(n)

"""