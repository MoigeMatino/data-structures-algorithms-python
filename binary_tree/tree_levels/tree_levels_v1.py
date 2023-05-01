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

NB:
Even though there is a nested for loop inside the while loop, the time complexity is still O(n) and not O(n^2).

Here's why:

    - The outer while loop runs at most n times because there are at most n nodes in the tree.
    - The inner for loop runs at most n times, because it processes all the nodes on the current level of the tree, and there are at most n nodes in the tree.
    - The number of times the inner for loop runs is proportional to the number of nodes in the tree, not the square of the number of nodes.

So the overall time complexity of the tree_levels function is O(n), not O(n^2).

"""
