from collections import deque


def bottom_right_value(root):
  """
  Finds the value of the rightmost node in the bottommost level of a binary tree.

  Args:
      root: The root node of the binary tree.

  Returns:
      The value of the rightmost node in the bottommost level, or None if the tree is empty.
  """

  if root is None:
    """
    # Check for empty tree
    If the root node is None, it indicates an empty tree. In this case, there's no bottom level 
    and no rightmost node to return. The function returns None.
    """
    return None

  queue = deque([root])
  """
  # Initialize a queue using deque
  We'll use a deque (double-ended queue) to perform a level-order traversal of the tree. A deque 
  is efficient for both appending and popping elements, making it suitable for this BFS (Breadth-First Search) approach.
  """

  while queue:
    """
    # Level-order traversal using a loop
    This loop continues as long as there are elements in the queue. It iterates through the nodes level by level.
    """
    current = queue.popleft()
    """
    # Process the current node
    The first node (leftmost) in the queue is retrieved and assigned to the 'current' variable. This node is then 
    removed from the queue using popleft().
    """

    if current.left is not None:
      """
      # Add left child to queue (if it exists)
      If the current node has a left child, it's appended to the queue. This ensures left children are processed 
      in the next iteration, maintaining the level-order traversal.
      """
      queue.append(current.left)

    if current.right is not None:
      """
      # Add right child to queue (if it exists)
      Similar to the left child, if the current node has a right child, it's added to the queue for processing in 
      the next iteration.
      """
      queue.append(current.right)

  return current.val


"""
BFS iterative approach
The reason we use BFS and not DFS is because DFS will get the right most value,
which may not necessarily be the BOTTOM right value. Consider this tree, DFS would return -13 
but the correct answer is 6. BFS will return the correct answer because of the way it traverses
the tree; level by level:
#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   -4   -13
#     / \       
#    -2  6

Time Complexity: O(n),
where n is the number of nodes in the tree. This is because the algorithm performs 
a level-order traversal, visiting each node exactly once.

Space Complexity: O(w), 
where w is the width of the widest level in the tree. The space complexity is determined 
by the maximum number of nodes that can be present in the queue at any given time. In the worst case, where the 
tree is a complete binary tree, all nodes in a particular level will be enqueued before processing, leading to a 
space complexity proportional to the width of the tree.

Further Notes:

This algorithm assumes a binary tree where each node can have at most two children (left and right).
The approach leverages a level-order traversal using a queue to ensure we process nodes level by level. By the time 
the loop finishes iterating through the queue, the current node will be the rightmost node in the bottommost level, 
as we process nodes from left to right within each level.
"""
