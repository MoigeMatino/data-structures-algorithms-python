from collections import deque

def how_high(node):
    """
    Calculates the height of a binary tree starting from a given node.

    Args:
    - node: The root node of the binary tree.

    Returns:
    - int: The height of the binary tree.

    """
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
Time Complexity Analysis:
- Each node is visited once: O(n), where n is the number of nodes in the binary tree.

Space Complexity Analysis:
- Queue storage: O(n) in the worst-case scenario where all nodes are enqueued.
Overall: O(n)

Further Notes:
- This function calculates the height of the binary tree using a breadth-first search (BFS) iterative approach.
  It traverses the tree level by level, counting the number of levels until reaching the bottom.
"""
