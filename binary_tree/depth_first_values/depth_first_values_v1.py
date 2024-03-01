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
    stack = [root]  # Initialize stack with the root node
    values = []  # List to store values of nodes in depth-first traversal order

    if root is None:  # If the tree is empty, return an empty list
        return []

    while stack:
        current = stack.pop()  # Pop a node from the stack
        values.append(current.val)  # Append the value of the current node to the values list

        if current.right:  # If the current node has a right child, push it to the stack
            stack.append(current.right)
        if current.left:  # If the current node has a left child, push it to the stack
            stack.append(current.left)

    return values  # Return the list of values in depth-first traversal order

"""
Time Complexity Analysis:
- Visiting each node once: O(n), where n is the number of nodes in the binary tree.
Overall: O(n)

Space Complexity Analysis:
- Storing nodes in the stack: O(h), where h is the height of the binary tree (worst-case scenario).
Overall: O(h)

Further Notes:
This algorithm performs a depth-first traversal of a binary tree iteratively using a stack. 
It starts from the root node and explores nodes in a depth-first manner, visiting the left child 
before the right child at each level. The values of the visited nodes are appended to a list 
in the order of traversal, and the final list of values is returned. The time complexity is 
O(n), where n is the number of nodes in the binary tree, and the space complexity is O(h), 
where h is the height of the binary tree in the worst-case scenario.
"""
