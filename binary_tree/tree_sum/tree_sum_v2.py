def tree_sum(root):
    """
    Calculates the sum of all node values in a binary tree recursively.

    Args:
        root (Node): The root node of the binary tree.

    Returns:
        int: The sum of all node values in the binary tree.

    """
    if root is None:  # If the root is None, return 0
        return 0
    
    left_sum = tree_sum(root.left)  # Recursively calculate the sum of left subtree nodes
    right_sum = tree_sum(root.right)  # Recursively calculate the sum of right subtree nodes

    return root.val + left_sum + right_sum  # Return the sum of node values including current node

"""
Time Complexity Analysis:
- Recursive calls: O(n), where n is the number of nodes in the binary tree.
Overall: O(n)

Space Complexity Analysis:
- Recursive call stack: O(h), where h is the height of the binary tree (worst-case scenario).
Overall: O(h)

Further Notes:
This algorithm calculates the sum of all node values in a binary tree using recursive traversal. 
It recursively calculates the sum of values for the left subtree and the right subtree, and then 
adds the value of the current node. The base case is when the root is None, in which case the 
function returns 0. The time complexity is O(n), where n is the number of nodes in the binary tree, 
and the space complexity is O(h), where h is the height of the binary tree in the worst-case scenario.
"""
