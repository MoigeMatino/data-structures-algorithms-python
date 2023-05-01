from collections import deque

def tree_levels(root):
    if root is None:
        return []
    
    queue = deque([root])
    level_nodes = []
    
    while queue:
        level = []
        
        for _ in range(len(queue)):
            current = queue.popleft()
            level.append(current.val)
            
            if current.left:
                queue.append(current.left)
            
            if current.right:
                queue.append(current.right)
        
        level_nodes.append(level)
    
    return level_nodes

"""
BFS iterative

n - number of nodes
Time: O(n)
Space: O(n)

"""