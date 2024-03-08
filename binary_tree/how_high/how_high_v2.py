from collections import deque

def how_high(node):
   """
  This function calculates the height of a binary tree using an iterative Breadth-First Search (BFS) approach.

  Args:
      node: The root node of the binary tree.

  Returns:
      The height of the binary tree, or -1 if the tree is empty.
  """

  # Check for empty tree
  if node is None:
    return -1  # Empty tree has a height of -1

  # Initialize variables
  queue = deque([node])  # Queue to store nodes for BFS traversal
  level = -1              # Counter for tree height (starts at -1 to account for root)

  while queue:
    """
    Iterate through the BFS traversal process until the queue is empty.
    """

    level_size = len(queue)  # Get the number of nodes in the current level

    # Process all nodes in the current level
    for _ in range(level_size):
      x = queue.popleft()      # Remove the first node from the queue

      # Add child nodes to the queue for exploration in the next level
      if x.right:
        queue.append(x.right)
      if x.left:
        queue.append(x.left)

    # Update level counter after processing all nodes in the current level
    level += 1

  return level
"""
Time Complexity Analysis:
- Each node is visited once: O(n), where n is the number of nodes in the binary tree.

Space Complexity Analysis:
Queue storage: O(n) in the worst-case scenario where all nodes are enqueued.
Overall: O(n)

Further Notes:
This algorithm utilizes an iterative BFS approach to traverse the tree. It maintains a queue to 
store nodes level-by-level. At each iteration, the algorithm processes all nodes in the current 
level (obtained using the queue size) by removing them from the front of the queue and adding 
their children to the back of the queue for exploration in the next level. This ensures that 
all nodes at a given level are processed before moving to the next level. The level counter is 
incremented after processing all nodes in the current level to track the tree's height.

This approach offers an efficient way to calculate the tree height with a time complexity of 
O(n) in most cases. BFS guarantees that all nodes are visited exactly once, making it 
suitable for scenarios where the order of node exploration is not crucial.
"""
"""
