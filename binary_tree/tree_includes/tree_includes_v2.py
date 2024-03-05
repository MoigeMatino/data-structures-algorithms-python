def tree_includes(root, target):
    """
    Checks if a binary tree contains a specific value using depth-first search recursively.

    Args:
        root (Node): The root node of the binary tree.
        target: The value to search for in the binary tree.

    Returns:
        bool: True if the target value is found in the binary tree, False otherwise.

    """
    if root is None:  # If the root is None, return False
        return False
    
    if root.val == target:  # If the value of the current node matches the target value, return True
        return True

    # Recursively check if the target value is present in the left or right subtree
    return tree_includes(root.left, target) or tree_includes(root.right, target)

"""
Time Complexity Analysis:
- Recursive calls: O(n), where n is the number of nodes in the binary tree.
Overall: O(n)

Space Complexity Analysis:
- Recursive call stack: O(h), where h is the height of the binary tree (worst-case scenario).
Overall: O(h)

Further Notes:
This algorithm checks if a binary tree contains a specific value using depth-first search recursively. 
It starts from the root node and recursively checks if the target value is present in the left or 
right subtree. If the target value is found in any subtree, the function returns True; otherwise, 
it returns False. The time complexity is O(n), where n is the number of nodes in the binary tree, 
and the space complexity is O(h), where h is the height of the binary tree in the worst-case scenario.
"""
