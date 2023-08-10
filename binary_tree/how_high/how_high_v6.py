from collections import deque
def how_high(node):
    if node is None:
        return -1

    queue = deque([(node, 0)])

    while queue:
        current_node, level = queue.popleft()

        if current_node.left:
            queue.append((current_node.left, level+1))

        if current_node.right:
            queue.append((current_node.right, level+1))

    return level

"""
n - # of nodes
Time: O(n)
Space: O(n)
"""