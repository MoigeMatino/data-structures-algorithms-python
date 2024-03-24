from statistics import mean


def level_averages(root):
    """
    Calculates the average value of nodes at each level in a binary tree using a Depth-First Search (DFS) approach.

    Args:
        root: The root node of the binary tree.

    Returns:
        A list of floats, where each element represents the average value of nodes at a specific level.
        An empty list is returned if the tree is empty.
    """

    levels = []
    fill_levels(root, levels, 0)  # Start filling levels from root at level 0

    avgs = []
    for level in levels:
        avgs.append(mean(level))  # Calculate average for each level
    return avgs


def fill_levels(root, levels, level_num):
    """
    Recursive helper function to fill a list with node values at each level in the tree.

    Args:
        root: The current node being processed.
        levels: A list to store nodes at each level.
        level_num: The current level number.
    """

    if root is None:
        return  # Base case: Do nothing if node is None

    if level_num == len(levels):
        levels.append([root.val])  # Create a new list for the level if it doesn't exist
    else:
        levels[level_num].append(root.val)  # Append node value to existing level list

    fill_levels(root.left, levels, level_num + 1)  # Process left child at next level
    fill_levels(root.right, levels, level_num + 1)  # Process right child at next level

"""
Time Complexity: O(n)
The algorithm visits each node in the tree once using a DFS approach. In the worst case, 
all nodes are visited, leading to a linear time complexity.

Space Complexity: O(n) in the worst case
The recursion can lead to a call stack size proportional to the tree height 
in the worst case scenario (e.g., a skewed tree).

"""
