def max_path_sum(grid: list[list[int]]) -> int:
    """
    Finds the maximum sum of a path through a grid of integers.

    Args:
        grid (list[list[int]]): A 2D grid represented as a list of lists, where each inner list represents a row.
            Elements are integers representing the value at that grid position.

    Returns:
        int: The maximum sum of a valid path from the top-left corner to the bottom-right corner of the grid.

    This function implements a memoized recursive strategy to find the maximum sum of a path
    through a given grid. A valid path starts from the top-left corner and reaches the
    bottom-right corner by moving only down or right. The sum of the path is calculated by
    adding the value at each grid position visited along the path.
    """

    # Delegate the actual calculation with memoization to the helper function
    return _max_path_sum(grid, 0, 0, {})

def _max_path_sum(grid: list[list[int]], r: int, c: int, memo: dict[tuple[int, int], int]) -> int:
    """
    Helper function for finding the maximum sum of a path through a grid from a specific position.

    Args:
        grid (list[list[int]]): A 2D grid represented as a list of lists.
        r (int): The current row index.
        c (int): The current column index.
        memo (dict[tuple[int, int], int]): A dictionary to store memoized results (position -> maximum sum).

    Returns:
        int: The maximum sum of a valid path from the current position to the bottom-right corner of the grid.
    """

    # Create a tuple to represent the current position (row, column) as a key for the memo
    pos = (r, c)

    # Check if the maximum sum from this position is already stored in the memo
    if pos in memo:
        return memo[pos]

    # Base case 1: Invalid position (outside grid boundaries)
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return float("-inf")  # Return negative infinity for invalid positions

    # Base case 2: Reached the destination (bottom-right corner)
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return grid[r][c]  # Return the value at the destination

    # Explore paths moving down and right (recursive calls)
    down_sum = _max_path_sum(grid, r + 1, c, memo)  # Find max sum moving down
    right_sum = _max_path_sum(grid, r, c + 1, memo)  # Find max sum moving right

    # Maximum sum from current position is the value at the current position + max(down_sum, right_sum)
    max_sum = grid[r][c] + max(down_sum, right_sum)

    # Store the maximum sum from this position in the memo and return it
    memo[pos] = max_sum
    return memo[pos]

# Time Complexity: O(r * c)
# - Memoization avoids redundant calculations for the maximum sum from each grid position.
# - Each position is visited at most once, and the maximum sum from that position is stored in the memo.
# - In the worst case, the function explores all possible paths, leading to a maximum of 'r' (rows) * 'c' (columns)
#   unique positions to visit. 

# Space Complexity: O(r * c)
#    - In the worst case, the `memo` dictionary can store the maximum sum for each unique position in the grid.
#    - There can be a maximum of 'r' (rows) * 'c' (columns) unique positions.
#    - Each entry in the memo dictionary stores a key (tuple of row and column indices) and a value (maximum sum).
#    - Assuming constant space for the key and value, the space complexity is dominated by the number of entries,
#      resulting in O(r * c).

# Approach:
# The approach utilizes memoization to optimize the problem. It stores previously computed results
# in a dictionary (`memo`) to avoid redundant calculations. When a specific grid position is encountered
# again, the stored value (maximum sum from that position) is retrieved instead of making another
# recursive call. This significantly improves the time complexity compared to the naive recursive approach.   
