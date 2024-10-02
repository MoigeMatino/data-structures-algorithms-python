class Node:
  def __init__(self, val):
      self.val = val
      self.right = None
      self.left = None

def serialise(root: Node) -> list:
    """
    Serialise a binary tree into a list using a pre-order traversal approach.
    The function uses a stack to traverse the tree iteratively and appends node
    values to a list. If a node is a leaf, it appends "None" to indicate the end
    of a branch.

    Parameters:
    root (Node): The root node of the binary tree.

    Returns:
    list: A list representing the serialised binary tree.
    """
    if not root:
        return None
    
    stack = [root]
    stream = []
    while stack:
        current = stack.pop()
        stream.append(current.val)
        
        # Append "None" to indicate the end of a branch
        if not current.right and not current.left:
            stream.append("None")
        
        # Push right child first so that left child is processed first
        if current.right:
            stack.append(current.right)
            
        if current.left:
            stack.append(current.left)
    return stream

def deserialise(stream: list) -> Node:
    """
    Deserialise a list back into a binary tree. The function reverses the list
    and uses a helper function to recursively reconstruct the tree.

    Parameters:
    stream (list): The list representing the serialised binary tree.

    Returns:
    Node: The root node of the deserialised binary tree.
    """
    stream.reverse()
    root = deserialise_helper(stream)
    return root

def deserialise_helper(stream: list) -> Node:
    """
    Helper function to recursively deserialise the list into a binary tree.

    Parameters:
    stream (list): The list representing the serialised binary tree.

    Returns:
    Node: The current node being reconstructed.
    """
    node_val = stream.pop()
    if isinstance(node_val, str) and node_val == "None":
        return None
    
    node = Node(node_val)
    node.left = deserialise_helper(stream)
    node.right = deserialise_helper(stream)
    
    return node

# Approach and Reasoning
# ----------------------
# The serialisation function uses an iterative pre-order traversal to convert the binary tree into a list.
# It uses a stack to manage the traversal order, ensuring that the left child is processed before the right child.
# "None" is appended to the list to indicate the end of a branch, which helps in reconstructing the tree during deserialisation.

# The deserialisation function reverses the list and uses a recursive helper function to reconstruct the tree.
# The helper function pops elements from the list, creating nodes and recursively setting their left and right children.
# The use of "None" in the list helps identify when a branch ends, allowing the function to return None for leaf children.

# Complexity Analysis
# -------------------
# Time Complexity:
# - Serialisation: O(n), where n is the number of nodes in the tree. Each node is visited once.
# - Deserialisation: O(n), where n is the number of nodes in the tree. Each node is reconstructed once.

# Space Complexity:
# - Serialisation: O(n), where n is the number of nodes in the tree. The list stores each node's value and "None" for leaves.
# - Deserialisation: O(h), where h is the height of the tree. This is due to the recursive call stack during reconstruction.