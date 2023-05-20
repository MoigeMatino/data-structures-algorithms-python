from collections import deque
    
def tree_levels(root):
    if root is None:
        return []
    
    levels = []
    queue = deque([ (root, 0) ])
    while queue:
        current, level_num = queue.popleft()
        
        if len(levels) == level_num:
            levels.append([ current.val ])
        else:
            levels[level_num].append(current.val)
        
        if current.left is not None:
            queue.append((current.left, level_num + 1))
        
        if current.right is not None:
            queue.append((current.right, level_num + 1))
    
    return levels   

"""
BFS iterative - Approach 2


n = number of nodes
Time: O(n)
Space: O(n)

"""