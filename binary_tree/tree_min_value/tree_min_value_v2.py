def tree_min_value(root):
    """
    Finds the minimum value in a binary tree using depth-first search recursively.

    Args:
        root (Node): The root node of the binary tree.

    Returns:
        int: The minimum value in the binary tree.

    """
    if root is None:  # Base case: If the root is None, return positive infinity
        return float("inf")
    
    # Recursively find the smallest value in the left subtree
    smallest_left_value = tree_min_value(root.left)
    # Recursively find the smallest value in the right subtree
    smallest_right_value = tree_min_value(root.right)
    
    # Return the minimum value among the current node value, smallest value in the left subtree,
    # and smallest value in the right subtree
    return min(root.val, smallest_left_value, smallest_right_value)

"""
Time Complexity Analysis:
- Recursive calls: O(n), where n is the number of nodes in the binary tree.
Overall: O(n)

Space Complexity Analysis:
- Recursive call stack: O(h), where h is the height of the binary tree (worst-case scenario).
Overall: O(h)

Further Notes:
This algorithm finds the minimum value in a binary tree using depth-first search recursively. 
It starts from the root node and recursively finds the smallest value in the left subtree 
and the smallest value in the right subtree. Then, it returns the minimum value among the 
current node value, smallest value in the left subtree, and smallest value in the right subtree. 
The time complexity is O(n), where n is the number of nodes in the binary tree, and the space 
complexity is O(h), where h is the height of the binary tree in the worst-case scenario.
"""
