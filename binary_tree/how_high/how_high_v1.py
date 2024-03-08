def how_high(node):
  """
  This function calculates the height of a binary tree using an iterative Depth-First Search (DFS) approach.

  Args:
      node: The root node of the binary tree.

  Returns:
      The height of the binary tree, or -1 if the tree is empty.
  """

  # Check for empty tree
  if node is None:
    return -1  # Empty tree has a height of -1

  # Initialize variables
  stack = [node]  # Stack to store nodes for DFS traversal
  level = -1      # Counter for tree height (starts at -1 to account for root)

  while stack:
    """
    Iterate through the DFS traversal process until the stack is empty.
    """

    new_level = []  # Temporary list to store children for the next level

    # Process all nodes in the current level
    for x in stack:
      # Add child nodes to the new level for exploration
      if x.right:
        new_level.append(x.right)
      if x.left:
        new_level.append(x.left)
      # Remove the current node from the stack
      stack.remove(x)

    # Update stack for the next level and increment height counter
    stack = new_level
    level += 1

  return level

"""
Time Complexity: O(n^2)

In the worst case, the tree may be completely skewed, meaning all nodes have only one child. 
In this scenario, the DFS traversal will visit each node and add its child to the stack. 
Since the stack can grow up to n nodes (all nodes in the skewed path), and each node is processed 
once, the time complexity becomes O(n) * O(n) = O(n^2).

Space Complexity: O(n)

The space complexity arises from the stack used for the DFS traversal. 
In the worst-case scenario (skewed tree), the stack can hold all nodes in the path from root to leaf, 
resulting in a space complexity of O(n).

Further Notes:

This algorithm utilizes an iterative DFS approach to traverse the tree. It maintains a stack 
to keep track of unvisited nodes. At each level, the algorithm iterates through the nodes in the 
current level, adding their children to the stack for exploration in the next level. It also removes 
the processed node from the stack. This process continues until the stack becomes empty, signifying 
that all nodes have been visited. The level counter is incremented at each level change to track 
the tree's height.

This approach offers an iterative solution to the tree height problem without the need for recursion. 
However, the time complexity can be O(n^2) in the worst case of a skewed tree due to redundant 
stack operationsthe removal operation in the stack traversal loop, makes it inefficient compared to other approaches).
If the tree structure is guaranteed to be balanced, alternative approaches like recursive DFS might achieve better time complexity (O(n)).
"""
