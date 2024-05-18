def count_paths(grid):
    """
    Count the number of unique paths from the top-left to the bottom-right corner of a grid,
    avoiding cells marked with 'X'.

    Args:
        grid (list of list of str): 2D grid where 'X' represents obstacles and other cells are free to traverse.

    Returns:
        int: Number of unique paths from the top-left to the bottom-right corner.
    """
    return _count_paths(grid, 0, 0)


def _count_paths(grid, r, c):
    """
    Helper function to recursively count the number of unique paths from a given cell (r, c) to the bottom-right corner,
    avoiding cells marked with 'X'.

    Args:
        grid (list of list of str): 2D grid where 'X' represents obstacles and other cells are free to traverse.
        r (int): Current row index.
        c (int): Current column index.

    Returns:
        int: Number of unique paths from cell (r, c) to the bottom-right corner.
    """
    # Base case: if out of bounds or cell is an obstacle, return 0
    if r == len(grid) or c == len(grid[0]) or grid[r][c] == 'X':
        return 0
    
    # Base case: if bottom-right cell is reached, return 1
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return 1
    
    # Recursively count the number of paths by moving down
    down_paths = _count_paths(grid, r + 1, c)
    
    # Recursively count the number of paths by moving right
    right_paths = _count_paths(grid, r, c + 1)

    # Return the sum of paths from the two possible moves (down and right)
    return down_paths + right_paths



# Time Complexity:
# The time complexity of this algorithm is O(2^(m+n)), where m is the number of rows and n is the number of 
# columns in the grid. This is because each cell can lead to two recursive calls, leading to an exponential number 
# of calls in the worst case.

# Space Complexity:
# The space complexity is O(m+n) due to the recursion stack. In the worst case, the maximum depth of the recursion 
# stack will be m+n.

# Approach and Reasoning:
# 1. The algorithm uses a recursive approach to explore all possible paths from the top-left corner to the bottom-right corner of the grid, avoiding obstacles.
# 2. For each cell, it counts the number of unique paths by considering the paths to the cell directly below and the cell directly to the right, skipping cells that are out of bounds or marked with 'X'.
# 3. Base cases are defined to handle out-of-bounds conditions or cells with obstacles (returning 0) and reaching the bottom-right corner (returning 1).
# 4. The result for each cell is the sum of the number of paths from the two possible moves (right and down).

# This naive recursive approach can be optimized using dynamic programming or memoization to avoid redundant calculations and improve efficiency.

