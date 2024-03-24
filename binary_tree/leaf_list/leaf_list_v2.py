def leaf_list(root):
    """
    Generates a list of leaf nodes' values in a binary tree using a recursive DFS approach.

    Args:
        root: The root node of the binary tree.

    Returns:
        A list of values of leaf nodes in the binary tree, or an empty list if the tree is empty.
    """

    leaves = []
    _leaf_list(root, leaves)  # Call the helper function to traverse and collect leaves
    return leaves


def _leaf_list(root, leaves):
    """
    Recursive helper function to traverse the tree and collect leaf node values.

    Args:
        root: The current node being processed.
        leaves: A list to store the collected leaf node values.
    """

    if root is None:
        return  # Base case: Do nothing if the node is None

    if root.left is None and root.right is None:
        leaves.append(root.val)  # Append leaf node value if it has no children

    _leaf_list(root.left, leaves)  # Recursively process the left child
    _leaf_list(root.right, leaves)  # Recursively process the right child

"""
Time Complexity: O(n), where n is the number of nodes
The algorithm visits each node in the tree once using a recursive DFS approach. 
In the worst case, all nodes are visited, leading to linear time complexity.

Space Complexity: O(n) in the worst case
The recursion can lead to a call stack size proportional to the tree height 
in the worst-case scenario (e.g., a skewed tree).

"""
