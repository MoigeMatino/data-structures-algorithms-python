def tree_value_count(root, target):
    if root is None:
        return 0
    
    match = 1 if root.val == target else 0

    left_count = tree_value_count(root.left, target)
    right_count = tree_value_count(root.right, target)

    return match + left_count + right_count
