class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def max_path_sum(root):
    """
    Finds the maximum path sum in a binary tree using a recursive approach.

    Args:
        root (Node): The root node of the binary tree.

    Returns:
        int: The maximum path sum in the binary tree.

    """
    if root is None:
        return float("-inf")  # If root is None, return negative infinity
    
    if root.left is None and root.right is None:
        return root.val  # If root has no children, return its value as the path sum
    
    # Recursively find the maximum path sum in the left and right subtrees
    max_left = max_path_sum(root.left)
    max_right = max_path_sum(root.right)
    
    # Return the maximum of the current node value and the sum of the maximum path sums of its children
    return root.val + max(max_left, max_right)

"""
Time Complexity Analysis:
- Each node is visited once: O(n), where n is the number of nodes in the binary tree.

Space Complexity Analysis:
- Recursive function calls: O(h), where h is the height of the binary tree (worst-case scenario).
- Stack space for recursion: O(h).
Overall: O(h)

Further Notes:
This algorithm recursively calculates the maximum path sum in a binary tree. It traverses the tree 
and calculates the maximum path sum for each node considering both left and right subtrees. The maximum 
path sum for a node is the maximum of its value and the sum of the maximum path sums of its children. 
The time complexity is O(n), where n is the number of nodes in the binary tree, and the space complexity 
is O(h), where h is the height of the binary tree in the worst-case scenario.

Another permutation of this problem is the Binary Tree Maximum Path Sum
This problem tries to find the maximum sum of any non-empty path that may or may not include 
the root. Checkout the 'max_tree_path_sum' entry in this directory to find out how to solve this problem.
"""

