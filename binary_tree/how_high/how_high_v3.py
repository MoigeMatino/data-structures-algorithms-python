def how_high(node):
    if node is None:
        return -1

    left_height = how_high(node.left)
    right_height = how_high(node.right)
    return 1 + max(left_height, right_height)

"""
DFS recursive approach

n = number of nodes
Time: O(n)
Space: O(n)

"""