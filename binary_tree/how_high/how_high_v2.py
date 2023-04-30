from collections import deque

def how_high(node):
    if node is None:
        return -1
    
    queue = deque([node])
    level = -1
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            x = queue.popleft()
            if x.right:
                queue.append(x.right)
            if x.left:
                queue.append(x.left)
        level += 1
    return level


"""
BFS iterative approach
n - number of nodes
Time: O(n)
Space: O(n)
"""