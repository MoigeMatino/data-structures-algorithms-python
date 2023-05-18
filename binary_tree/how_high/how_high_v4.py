from collections import deque

def how_high(node):
    if node is None:
        return -1

    level = 0
    queue = deque([(node,0)])

    while queue:

        level_size = len(queue)
        for _ in range(level_size):
            x, level = queue.popleft()
            if x.right:
                queue.append((x.right, level+1))
            if x.left:
                queue.append((x.left, level+1))
        
    return level

"""

n = number of nodes
Time: O(n)
Space: O(n)

"""

