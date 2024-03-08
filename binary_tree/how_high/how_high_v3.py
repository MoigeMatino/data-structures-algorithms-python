def how_high(node):
  """
  This function calculates the height of a binary tree using a recursive approach.

  Args:
      node: The root node of the binary tree.

  Returns:
      The height of the binary tree, or -1 if the tree is empty.
  """

  # Base case: Empty tree
  if node is None:
    return -1  # Empty tree has a height of -1

  # Recursive calls to calculate left and right subtrees' heights
  left_height = how_high(node.left)
  right_height = how_high(node.right)

  # Return the height of the current node (1 + max(left, right))
  return 1 + max(left_height, right_height)


"""
Time Complexity Analysis:
- Each node is visited once: O(n), where n is the number of nodes in the binary tree.

Space Complexity Analysis:
- Recursive function calls: O(h), where h is the height of the binary tree (worst-case scenario).
- Stack space for recursion: O(h).
Overall: O(h)

Further Notes:
This algorithm implements a recursive approach to calculate the height of a binary tree. 
It works by checking for the base case (empty tree) and then recursively calling itself 
on the left and right subtrees to obtain their heights. Finally, it returns 1 (for the current 
node) plus the maximum height found from the left and right subtrees.
"""
