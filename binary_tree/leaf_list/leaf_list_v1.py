def leaf_list(root):
    if root is None:
        return []
    
    stack = [root]
    leaf_list = []
    
    while stack:
        current = stack.pop()
        
        if current.right is not None:
            stack.append(current.right)
        
        if current.left is not None:
            stack.append(current.left)    
        
        if current.left is None and current.right is None:
            leaf_list.append(current.val)     
        
    return leaf_list