def path_finder(root, target):
    result = _path_finder(root, target)
    if result is None:
        return None
    else:
        return result[::-1]

def _path_finder(root, target):
    if root is None:
        return None
    
    if root.val == target:
        return [root.val]
    
    left_path = _path_finder(root.left, target)
    if left_path is not None:
        left_path.append(root.val)
        return left_path
    right_path = _path_finder(root.right, target)
    if right_path is not None:
        right_path.append(root.val)
        return right_path    
    return None

"""
Depth first approach
More efficient solution by using append which runs in costant time


n = number of nodes
Time: O(n)
Space: O(n)

"""