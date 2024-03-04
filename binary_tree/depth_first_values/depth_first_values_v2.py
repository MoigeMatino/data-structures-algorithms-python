class Node:
    """
    Class representing a node in a binary tree.

    Attributes:
        val: The value stored in the node.
        left: Reference to the left child node.
        right: Reference to the right child node.

    """

    def __init__(self, val):
        """
        Initializes a node with the given value.

        Args:
            val: The value to be stored in the node.

        """
        self.val = val
        self.left = None
        self.right = None


def depth_first_values(root):
    """
    Performs depth-first traversal of a binary tree and returns the values of the nodes in the traversal order.

    Args:
        root (Node): The root node of the binary tree.

    Returns:
        list: A list containing the values of the nodes in depth-first traversal order.

    """
    if root is None:  # If the tree is empty, return an empty list
        return []

    # Recursively get the values of nodes in the right subtree
    right_values = depth_first_values(root.right)
    # Recursively get the values of nodes in the left subtree
    left_values = depth_first_values(root.left)

    # Concatenate the values of the current node, left subtree, and right subtree
    return [root.val, *left_values, *right_values]

"""
Time Complexity Analysis:
- Visiting each node once: O(n), where n is the number of nodes in the binary tree.
Overall: O(n)

Space Complexity Analysis:
- Storing values of nodes in recursive function calls: O(h), where h is the height of the binary tree (worst-case scenario).
Overall: O(h)

Further Notes:
This algorithm performs a depth-first traversal of a binary tree recursively. It starts from the root node 
and recursively traverses the left subtree, followed by the right subtree. The values of the nodes are 
appended to a list in the order of traversal, and the final list of values is returned. The time complexity 
is O(n), where n is the number of nodes in the binary tree, and the space complexity is O(h), where h is 
the height of the binary tree in the worst-case scenario.
"""
