def all_tree_paths(root):
  """
  Finds all root-to-leaf paths in a binary tree.

  Args:
      root: The root node of the binary tree.

  Returns:
      A list of lists, where each inner list represents a path from the root to a leaf node.

    Example:
    >>> root = Node(1)
    >>> root.left = Node(2)
    >>> root.right = Node(3)
    >>> root.left.left = Node(4)
    >>> root.left.right = Node(5)
    >>> all_tree_paths(root)
    [[1, 2, 4], [1, 2, 5], [1, 3]]
  """

  if root is None:
    """
    # Check for empty tree
    If the root node is None, it indicates an empty tree. There are no paths in an empty tree, 
    so the function returns an empty list.
    """
    return []

  if root.left is None and root.right is None:
    """
    # Base case: Leaf node
    If the current node is a leaf node (no left or right children), it represents a single-element path 
    containing only the value of that node. We return a list with this single-element list.
    """
    return [[root.val]]

  paths = []
  """
  # Initialize an empty list for paths
  This list will store all the root-to-leaf paths found during the recursive calls.
  """

  left_sub_paths = all_tree_paths(root.left)
  """
  # Recursive call for left subtree
  The function recursively calls itself on the left subtree to find all paths originating from the left child.
  """
  for sub_path in left_sub_paths:
    """
    # Process left subtree paths
    Iterate through each path found in the left subtree.
    """
    new_path = [*sub_path][::-1] + [root.val]
    """
    # Construct new path from left subtree
    A new path is created by:
      1. Reversing the sub_path from the left subtree (to maintain root-to-leaf order).
      2. Appending the current root's value to the beginning of the reversed sub_path.
    This new path represents a path starting from the current root, going down the left subtree, 
    and incorporating the sub_path found there.
    """
    paths.append(new_path[::-1])
    """
    # Append reversed new path to results
    The newly constructed path is reversed again to ensure the correct root-to-leaf order and appended 
    to the 'paths' list.
    """

  right_sub_paths = all_tree_paths(root.right)
  """
  # Recursive call for right subtree
  Similar to the left subtree, the function calls itself recursively on the right subtree to find paths 
  originating from the right child.
  """
  for sub_path in right_sub_paths:
    """
    # Process right subtree paths
    Similar to the left subtree, process each path found in the right subtree.
    """
    new_path = [*sub_path][::-1] + [root.val]
    """
    # Construct new path from right subtree (same logic as left subtree)
    A new path is constructed following the same logic as the left subtree, considering the right subtree's paths.
    """
    paths.append(new_path[::-1])
    """
    # Append reversed new path to results (same logic as left subtree)
    The newly constructed path is appended to the 'paths' list after reversing it for the correct order.
    """

  return paths

"""

Time Complexity Analysis:
In the worst case, the algorithm traverses all nodes in the binary tree, hence the time complexity 
is O(n), where n is the number of nodes in the tree.

Space Complexity Analysis:
The space complexity depends on the number of paths generated. In the worst case, when every node is 
on the path to the root, the space complexity is O(n), where n is the number of nodes in the tree.

Further Notes
Approach Reasoning:
The recursive approach allows us to efficiently explore all paths in a binary tree. It works by:

    Base Case:
    If the current node is a leaf node (no children), it represents a single-element path (containing only the value of that node). We return a list with this single-element list.
    
    Recursive Calls:
        The function makes recursive calls to its left and right subtrees. These calls essentially explore all possible paths originating from the left and right children of the current node.
        Each recursive call returns a list of paths found in the respective subtree.
        
    Path Construction:
        For each path (sub_path) returned from the subtrees:
            We reverse the sub_path (as it represents a path from a leaf node up to the current node). This ensures the final paths have the correct root-to-leaf order.
            We prepend the current node's value (root.val) to the beginning of the reversed sub-path. This creates a new path that starts from the current root, goes down (either left or right 
            subtree based on the recursive call), and incorporates the sub-path found there.
        The newly constructed path is then appended to the paths list.

By recursively exploring both subtrees and constructing new paths by combining sub-paths with the current node's value, this approach efficiently finds all possible root-to-leaf paths in the binary tree.

Choice of Recursive Approach:

A recursive approach is well-suited for this problem because the structure of a binary tree naturally lends itself to a divide-and-conquer strategy. Each node can be considered a subproblem, and the 
solution for the entire tree can be built by combining the solutions for its left and right subtrees. The recursive calls handle the exploration of these subtrees, resulting in a clear and elegant 
solution for finding all root-to-leaf paths.


"""
