from collections import deque

def tree_value_count(root, target):
    """
    Count the occurrences of a target value in the binary tree using iterative breadth-first traversal.

    Args:
    - root: The root node of the binary tree.
    - target: The value to count occurrences of.

    Returns:
    - int: The number of occurrences of the target value in the binary tree.

    """

    # Base case: If the root is None, return 0
    if root is None:
        return 0
    
    # Initialize a queue for iterative breadth-first traversal
    queue = deque([root])
    count = 0

    # Iterate through the binary tree using iterative breadth-first traversal
    while queue:
        current = queue.popleft()

        # If the value of the current node matches the target value, increment count
        if current.val == target:
            count += 1

        # Add the right child to the queue if it exists
        if current.right is not None:
            queue.append(current.right)

        # Add the left child to the queue if it exists
        if current.left is not None:
            queue.append(current.left)

    return count

"""
Time Complexity Analysis:
- Each node is visited once: O(n), where n is the number of nodes in the binary tree.

Space Complexity Analysis:
- Queue space for iterative traversal: O(n), where n is the number of nodes in the binary tree to be stored in the queue
(worst-case scenario).
Overall: O(n)

Further Notes:
Iterative breadth-first traversal is used to traverse the binary tree level by level.
At each level, the algorithm checks if the value of the node matches the target value.
If it matches, it increments the count by 1.
The algorithm iterates through the tree while maintaining a queue of nodes to visit next.
This approach avoids using recursion and instead uses a queue to keep track of nodes to visit.
"""
