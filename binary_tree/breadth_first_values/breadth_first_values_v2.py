from collections import deque
class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def breadth_first_values(root):
    if not root:
        return []
    
    values = []
    queue = deque([root])# * adding element to deque

    while queue:
        current = queue.popleft()# * takes O(1), constant time
        values.append(current)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
        
    return values

"""
n - # of nodes
Time: O(n)
Space: O(n)

"""

