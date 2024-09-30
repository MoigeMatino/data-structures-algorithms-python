def calculate_diameter(root):
    """
    Calculate the diameter of a binary tree. The diameter is defined as the
    length of the longest path between any two nodes in the tree. This path
    may or may NOT pass through the root.

    Parameters:
    root (Node): The root node of the binary tree.

    Returns:
    int: The diameter of the tree.
    """
    if root is None:
        return 0

    # Calculate the height of the left and right subtrees
    # The addition of 1 ensures that each node's height calculation includes 
    # the edge connecting it to its tallest child, in this case, the root node
    left_height = 1 + calculate_height(root.left)
    right_height = 1 + calculate_height(root.right)

    # Calculate the diameter passing through the root
    through_root_diameter = left_height + right_height

    # Calculate the diameter of the left and right subtrees
    left_diameter = calculate_diameter(root.left)
    right_diameter = calculate_diameter(root.right)

    # The diameter is the maximum of the three possible diameters
    return max(left_diameter, right_diameter, through_root_diameter)

def calculate_height(root):
    """
    Calculate the height of a binary tree. The height is defined as the number
    of edges in the longest path from the node to a leaf.

    Parameters:
    root (Node): The root node of the binary tree.

    Returns:
    int: The height of the tree.
    """
    if root is None:
        return -1

    # Calculate the height of the left and right subtrees
    left_height = calculate_height(root.left)
    right_height = calculate_height(root.right)

    # The height of the current node is 1 plus the maximum of the heights of its subtrees
    return 1 + max(left_height, right_height)