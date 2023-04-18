class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def breadth_first_values(root):
    if not root:
        return []
    
    values = []
    queue = [root]

    while queue:
        current = queue.pop(0)
        values.append(current)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
        
    return values

"""
n - # of nodes
Time: O(n^2) ; this is because popping elements from a list takes O(n) time then include O(n) from looping through all elements
Space: O(n)

"""

