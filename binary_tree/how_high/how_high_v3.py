def how_high(node):
    """
    Calculates the height of a binary tree starting from a given node(root).

    Args:
    - node: The root node of the binary tree.

    Returns:
    - int: The height of the binary tree.    
    """
    if node is None:
        return -1

    left_height = how_high(node.left)
    right_height = how_high(node.right)
    return 1 + max(left_height, right_height)

"""
Time Complexity Analysis:
- Each node is visited once: O(n), where n is the number of nodes in the binary tree.

Space Complexity Analysis:
- Recursive function calls: O(h), where h is the height of the binary tree (worst-case scenario).
- Stack space for recursion: O(h).
Overall: O(h)

Further Notes:
- This function recursively calculates the height of the binary tree by considering the maximum height of its
  left and right subtrees and adding 1 to account for the current node. The base case is when the node is None,
  in which case the height is -1.
"""
