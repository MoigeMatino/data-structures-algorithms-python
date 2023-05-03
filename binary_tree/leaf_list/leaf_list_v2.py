def leaf_list(root):
    leaves = []
    _leaf_list(root, leaves)
    return leaves

def _leaf_list(root, leaves):
    if root is None:
        return []
    
    if root.left is None and root.right is None:
        leaves.append(root.val)
        
    _leaf_list(root.left, leaves)
    _leaf_list(root.right, leaves)