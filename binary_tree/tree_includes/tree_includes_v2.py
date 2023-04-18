def tree_includes(root, target):
    if root is None:
        return 0
    
    if root.val == target:
        return True

    return tree_includes(root.left, target) or tree_includes(root.right, target)

"""
Depth first approach

n = number of nodes
Time: O(n)
Space: O(n)

"""