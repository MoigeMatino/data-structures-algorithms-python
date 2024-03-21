from collections import deque

def tree_levels(root):
   """
   Collects the values of a binary tree's nodes level-by-level using Breadth-First Search (BFS).

   Args:
       root: The root node of the binary tree.

   Returns:
       A list of lists, where each inner list represents the values of the nodes at a single level of the tree.
       If the tree is empty, returns an empty list.
   """

   if root is None:  # Check for empty tree
       return []

   levels = []  # Initialize list to store nodes per level
   queue = deque([(root, 0)])  # Initialize queue with root and its level

   while queue:  # Continue until all nodes are processed
       current, level_num = queue.popleft()  # Get current node and its level

       if len(levels) == level_num:  # Create a new level list if needed
           levels.append([current.val])
       else:  # Append to existing level list
           levels[level_num].append(current.val)

       # Add children to queue for processing, along with their levels
       if current.left is not None:
           queue.append((current.left, level_num + 1))
       if current.right is not None:
           queue.append((current.right, level_num + 1))

   return levels  # Return the list of levels

"""
**Time and Space Complexity:**

- Time Complexity: O(n), where n is the number of nodes in the tree. Each node is visited and processed once.
- Space Complexity: O(n), due to the queue and levels list, which can store up to n nodes in the worst case.

**Approach and Reasoning:**

- This algorithm uses Breadth-First Search (BFS) to traverse the tree level by level.
- A queue (`deque`) is employed to maintain the order of nodes to be processed, ensuring nodes are explored in the order they were encountered.
- Each node in the queue is paired with its level (`level_num`) to track which level it belongs to.
- The `levels` list dynamically grows as new levels are encountered, eliminating the need to pre-allocate space for all levels.
- This approach avoids recursion, making it suitable for large trees or those with potential stack overflow issues.

"""
