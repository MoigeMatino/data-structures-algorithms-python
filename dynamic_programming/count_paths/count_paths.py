def count_paths(grid: list[list[str]]) -> int:
    """
    Counts the number of valid paths from the top-left corner to the bottom-right corner of a grid.

    Args:
        grid (list[list[str]]): A 2D grid represented as a list of lists, where each inner list represents a row.
            Elements can be either '.' (valid path) or 'X' (obstacle).

    Returns:
        int: The number of valid paths from the top-left corner to the bottom-right corner.

    This function implements a memoized recursive approach to count the number of valid paths
    through a given grid. A valid path starts from the top-left corner and reaches the 
    bottom-right corner by moving only down or right, avoiding obstacles ('X').
    """
    # create hash map to cache subproblem results
    memo = {}

    # Delegate the actual calculation with memoization to the helper function
    return _count_paths(grid, 0, 0, memo)

def _count_paths(grid: list[list[str]], r: int, c: int, memo: dict[tuple[int, int], int]) -> int:
    """
    Helper function for counting valid paths through a grid from a specific position.

    Args:
        grid (list[list[str]]): A 2D grid represented as a list of lists.
        r (int): The current row index.
        c (int): The current column index.
        memo (dict[tuple[int, int], int]): A dictionary to store memoized results (position -> number of paths).

    Returns:
        int: The number of valid paths from the current position to the bottom-right corner.
    """

    # Create a tuple to represent the current position (row, column) as a key for the memo
    pos = (r, c)

    # Check if the number of paths from this position is already stored in the memo
    if pos in memo:
        return memo[pos]

    # Base case 1: Invalid position (outside grid or through a wall)
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 'X':
        return 0

    # Base case 2: Reached the destination (bottom-right corner)
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return 1

    # Explore paths moving down and right (recursive calls)
    down_paths = _count_paths(grid, r + 1, c, memo)  # Count paths moving down
    right_paths = _count_paths(grid, r, c + 1, memo)  # Count paths moving right

    # Total paths from this position is the sum of down and right paths
    total_paths = down_paths + right_paths

    # Store the total number of paths from this position in the memo and return it
    memo[pos] = total_paths
    return memo[pos]

# Time Complexity: O(r * c)
# - Memoization avoids redundant calculations for the number of paths from each grid position.
# - Each position is visited at most once, and the number of paths from that position is stored in the memo.
# - In the worst case, the function explores all possible paths, leading to a maximum of 'r' (rows) * 'c' (columns)
#   unique positions to visit. This results in a time complexity of O(r * c).

# Space Complexity: O(r * c)
# - The memo dictionary stores the number of paths for each visited position.
# - In the worst case, the memo can store values for all 'r' * 'c' positions, leading to a space complexity of O(r * c).
