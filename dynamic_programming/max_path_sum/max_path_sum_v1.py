def max_path_sum(grid):
    """
    Calculate the maximum path sum from the top-left to the bottom-right corner of a grid.

    Args:
        grid (list of list of int): 2D grid of integers.

    Returns:
        int: Maximum path sum.
    """
    return _max_path_sum(grid, 0, 0)


def _max_path_sum(grid, r, c):
    """
    Helper function to recursively calculate the maximum path sum from a given cell (r, c) to the bottom-right corner.

    Args:
        grid (list of list of int): 2D grid of integers.
        r (int): Current row index.
        c (int): Current column index.

    Returns:
        int: Maximum path sum from cell (r, c) to the bottom-right corner.
    """
    # Base case: if out of bounds, return negative infinity
    if r == len(grid) or c == len(grid[0]):
        return float("-inf")

    # Base case: if bottom-right cell is reached, return its value
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return grid[r][c]

    # Recursively calculate the maximum path sum for the cell directly below
    down_path_sum = _max_path_sum(grid, r + 1, c)

    # Recursively calculate the maximum path sum for the cell directly to the right
    right_path_sum = _max_path_sum(grid, r, c + 1)

    # Return the value of the current cell plus the maximum of the sums of the two possible paths
    return grid[r][c] + max(right_path_sum, down_path_sum)


# Time Complexity:
# The time complexity of this algorithm is O(2^(m+n)), where m is the number of rows and n is the number of columns in the grid. 
# This is because each cell can lead to two recursive calls, leading to an exponential number of calls in the worst case.

# Space Complexity:
# The space complexity is O(m+n) due to the recursion stack. In the worst case, the maximum depth of the recursion stack will be m+n.

# Further Notes:

# Approach and Reasoning:
# 1. The algorithm uses a recursive approach to explore all possible paths from the top-left corner to the bottom-right corner of the grid.
# 2. For each cell, it calculates the maximum path sum by considering the paths to the cell directly below and the cell directly to the right.
# 3. Base cases are defined to handle out-of-bounds conditions (returning negative infinity) and reaching the bottom-right corner (returning the value of that cell).
# 4. The result for each cell is the value of the current cell plus the maximum of the sums of the two possible paths (right and down).

# This naive recursive approach can be optimized using dynamic programming or memoization to avoid redundant calculations and improve efficiency.

