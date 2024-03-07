def path_finder(root, target):
    """
    Find a path from the root of the binary tree to a node with the target value.

    Args:
    - root: The root node of the binary tree.
    - target: The value of the node to find.

    Returns:
    - list or None: A list representing the path from the root to the target node if found,
      or None if the target node is not found.

    """

    # Call the helper function to perform the depth-first search
    result = _path_finder(root, target)

    # If the result is None, return None; otherwise, reverse the result list and return it
    if result is None:
        return None
    else:
        return result[::-1]


def _path_finder(root, target):
    """
    Helper function to recursively search for the target node in the binary tree.

    Args:
    - root: The current root node being processed.
    - target: The value of the node to find.

    Returns:
    - list or None: A list representing the path from the root to the target node if found,
      or None if the target node is not found.

    """

    # Base case: If the root is None, return None
    if root is None:
        return None
    
    # Base case: If the value of the current node matches the target value, return a list
    # containing only the value of the current node
    if root.val == target:
        return [root.val]
    
    # Recursive case: Search for the target value in the left subtree
    left_path = _path_finder(root.left, target)
    if left_path is not None:
        # If the target is found in the left subtree, append the current node's value
        # to the left_path list and return it
        left_path.append(root.val)
        return left_path
    
    # Recursive case: Search for the target value in the right subtree
    right_path = _path_finder(root.right, target)
    if right_path is not None:
        # If the target is found in the right subtree, append the current node's value
        # to the right_path list and return it
        right_path.append(root.val)
        return right_path
    
    # If the target value is not found in the current subtree, return None
    return None

"""
Time Complexity Analysis:
- Each node is visited once: O(n), where n is the number of nodes in the binary tree.

Space Complexity Analysis:
- Recursive function calls: O(h), where h is the height of the binary tree (worst-case scenario).
- Stack space for recursion: O(h).
Overall: O(h)

Further Notes:
More efficient solution by using append which runs in constant time.
We use the depth-first recursive approach because recursion inherently 
utilizes the call stack, allowing for accurate retrieval of path values.

The time complexity of this algorithm is O(n), where n is the number of nodes in the binary tree.
This is because in the worst-case scenario, the algorithm may need to visit every node in the tree
to find the target node.

The space complexity of this algorithm is also O(n), as the recursive calls consume space on the call stack
proportional to the height of the binary tree. In the worst case, the binary tree is skewed, leading to a
height of n and thus requiring O(n) space.

"""
