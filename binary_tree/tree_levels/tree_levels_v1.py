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

   if root is None:  # Handle empty tree case
       return []

   queue = deque([root])  # Initialize queue with the root node
   level_nodes = []  # List to store nodes for each level

   while queue:  # Continue until the queue is empty
       current_level_nodes = []  # List to store nodes at the current level

       for _ in range(len(queue)):  # Process all nodes at the current level
           current = queue.popleft()  # Get the first node from the queue
           current_level_nodes.append(current.val)   # Append its value to the current level's list

           if current.left:  # Add children to the queue for processing in subsequent levels
               queue.append(current.left)
           if current.right:
               queue.append(current.right)

       level_nodes.append(current_level_nodes)  # Add the completed level to the result list

   return level_nodes  # Return the list of levels

"""
**Time and Space Complexity:**

- Time Complexity: O(n), where n is the number of nodes in the tree. Each node is visited once.
- Space Complexity: O(n), due to the queue and level_nodes list, which can store up to n nodes in the worst case.

**Approach and Reasoning:**

- This algorithm employs a BFS approach, iteratively visiting nodes level by level.
- It leverages a queue data structure to maintain the order of nodes to be processed.
- It avoids recursion, making it suitable for large trees or those with potential stack overflow issues.
- It explicitly tracks the current level to group nodes correctly.
"""
