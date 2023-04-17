class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def depth_first_values(root):
    if root is None:
        return []
    right_values = depth_first_values(root.right)
    left_values = depth_first_values(root.left)

    return [root.val, *left_values, *right_values]