from collections import deque
def bottom_right_value(root):
    if root is None:
        return None
    queue = deque([root])
    while queue:
        current = queue.popleft()
        
        if current.left is not None:
                queue.append(current.left)
        
        if current.right is not None:
            queue.append(current.right)
        
    return current.val

"""
BFS iterative approach

n = number of nodes
Time: O(n)
Space: O(n)

"""