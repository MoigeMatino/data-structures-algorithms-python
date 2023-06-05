def all_tree_paths(root):
    if root is None:
        return []
    
    if root.left is None and root.right is None:
        return [ [root.val] ]
    
    paths = []

    left_sub_paths = all_tree_paths(root.left)
    for sub_path in left_sub_paths:
        new_path = [ *sub_path][::-1] + [root.val ]
        paths.append(new_path[::-1])
        """
        for sub_path in left_sub_paths:
            paths.append([ root.val, *sub_path ])
            
        the operation above ie adding a umber of values to the end of
        of the areay takes O(n) time resulting in an overral O(n^2)
        
        """
        
    right_sub_paths = all_tree_paths(root.right)
    for sub_path in right_sub_paths:
        new_path = [ *sub_path][::-1] + [root.val ]
        paths.append(new_path[::-1])
        """
        for sub_path in right_sub_paths:
            paths.append([ root.val, *sub_path ])
        """
    
    return paths

"""
DFS recursive

n = number of nodes
Time: O(n)
Space: O(n)

"""