def leaf_list(root):
   """
   Generates a list of leaf nodes' values in a binary tree using a Depth-First Search (DFS) approach.

   Args:
       root: The root node of the binary tree.

   Returns:
       A list of values of leaf nodes in the binary tree, or an empty list if the tree is empty.
   """

   if root is None:  # Handle empty tree case
       return []

   stack = [root]  # Initialize stack with root node
   leaf_list = []  # List to store leaf node values

   while stack:
       current = stack.pop()  # Pop the top node from the stack

       # Check if the current node is a leaf node (has no children)
       if current.right is None and current.left is None:
           leaf_list.append(current.val)  # Append leaf node value to the list

       # Otherwise, add children to the stack for further exploration (right child first, then left child)
       else:
           if current.right is not None:
               stack.append(current.right)
           if current.left is not None:
               stack.append(current.left)

   return leaf_list  # Return the list of leaf node values
"""
Time Complexity: O(n), where n is the number of nodes
The algorithm visits each node in the tree once using DFS. In the worst case, all nodes are visited,
leading to linear time complexity.

Space Complexity: O(n) in the worst case
The stack can hold up to a maximum of n/2 nodes in a skewed tree, resulting in linear space complexity.

"""
