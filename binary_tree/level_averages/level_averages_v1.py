from collections import deque
from statistics import mean


def level_averages(root):
    """
    Calculates the average value of nodes at each level in a binary tree.

    Args:
        root: The root node of the binary tree.

    Returns:
        A list of floats, where each element represents the average value of nodes at a specific level.
        An empty list is returned if the tree is empty.
    """

    if root is None:
        return []  # Handle empty tree case

    queue = deque([(root, 0)])  # Initialize queue with root and level 0
    level_averages = []  # List to store nodes at each level

    while queue:
        current, level = queue.popleft()  # Dequeue the next node and its level

        # Check if a new level needs to be created in level_averages
        if len(level_averages) == level:
            level_averages.append([current.val])  # Create a new list for the level
        else:
            level_averages[level].append(current.val)  # Append node value to existing level list

        # Add child nodes to the queue for processing
        if current.left:
            queue.append((current.left, level + 1))
        if current.right:
            queue.append((current.right, level + 1))

    # Calculate the average value for each level
    avgs = [mean(level) for level in level_averages]

    return avgs

"""
Time Complexity: O(n) where n is the number of nodes in the tree.
The algorithm visits each node in the tree once using a Breadth-First Search (BFS) approach.

Space Complexity: O(n) in the worst case.
Reason: The queue can hold all nodes in the tree in the worst-case scenario of a complete binary tree.

Further Notes:
- The `mean` function from the `statistics` module is used to calculate the average efficiently.
"""
