def tree_value_count(root, target):
    """
    Count the occurrences of a target value in the binary tree.

    Args:
    - root: The root node of the binary tree.
    - target: The value to count occurrences of.

    Returns:
    - int: The number of occurrences of the target value in the binary tree.

    """

    # Base case: If the root is None, return 0
    if root is None:
        return 0
    
    # Check if the value of the current node matches the target value
    match = 1 if root.val == target else 0

    # Recursive case: Count occurrences of the target value in the left and right subtrees
    left_count = tree_value_count(root.left, target)
    right_count = tree_value_count(root.right, target)

    # Return the sum of the occurrences in the current node, left subtree, and right subtree
    return match + left_count + right_count

"""
Time Complexity Analysis:
- Each node is visited once: O(n), where n is the number of nodes in the binary tree.

Space Complexity Analysis:
- Recursive function calls: O(h), where h is the height of the binary tree (worst-case scenario).
Overall: O(h)

Further Notes:
Depth-first traversal (recursive) is used to traverse the binary tree.
At each node, the algorithm checks if the value of the node matches the target value.
If it matches, it increments the count by 1. Then, it recursively counts occurrences 
of the target value in the left and right subtrees.
The total count is the sum of matches in the current node, left subtree, and right subtree.
"""
