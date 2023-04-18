def tree_min_value(root):
    if root is None:
        return float("inf")
    smallest_left_value = tree_min_value(root.left)
    smallest_right_value = tree_min_value(root.right)
    return min(root.val, smallest_left_value, smallest_right_value)

"""
DFS recursive approach

n = number of nodes
Time: O(n)
Space: O(n)

"""