from typing import List, Dict, Set, Tuple, Union


def find_min_distance_to_zero(mat: List[List[int]]) -> Dict[Tuple[int, int], int]:
  """
  Finds the minimum distances to all cells containing the value 0 in a matrix using memoization.

  This function takes a 2D matrix represented as a list of lists of integers as input.
  It uses a recursive approach with memoization to efficiently calculate the minimum
  distance from each cell to the nearest cell containing the value 0.

  Args:
      mat: A 2D list of integers representing the matrix.

  Returns:
      A dictionary mapping each cell's coordinates (represented as a tuple) to its
      minimum distance to a cell containing 0. If a cell is unreachable from any 0 cell,
      the distance is set to infinity (`float("inf")`).
  """

  rows = len(mat)  # Get the number of rows in the matrix
  cols = len(mat[0])  # Get the number of columns in the matrix

  # Initialize a dictionary to store minimum distances with memoization
  memo = {}

  # Iterate through the matrix and calculate distances for each cell
  for r in range(rows):
    for c in range(cols):
      visited = set()  # Create a set to keep track of visited cells (for this specific call)
      _find_min_distance_to_zero(mat, r, c, visited, memo)  # Recursive helper function

  return memo


def _find_min_distance_to_zero(
    mat: List[List[int]], r: int, c: int, visited: Set, memo: Dict[Tuple[int, int], int]
) -> Union[int, float]:
  """
  Recursive helper function to calculate the minimum distance to a 0 cell.

  This function takes the matrix, a cell's coordinates (`r`, `c`), a visited set,
  and a memoization dictionary as input. It checks if the distance for this cell
  is already stored in the memo. If not, it performs the following steps:
  1. Checks if the cell is out of bounds or has already been visited (presence in the visited set).
  2. If the cell contains 0, sets its distance to 0 and stores it in the memo.
  3. Recursively explores neighboring cells (up, down, left, right) and calculates
     the minimum distance from each neighbor to a 0 cell (adding 1 for the current step).
  4. Stores the minimum distance for the current cell in the memo and returns it.

  Args:
      mat: A 2D list of integers representing the matrix.
      r: The row coordinate of the current cell.
      c: The column coordinate of the current cell.
      visited: A set to track visited cells within this specific recursive call.
      memo: A dictionary to store minimum distances with memoization.

  Returns:
      The minimum distance from the current cell to a cell containing 0,
      or infinity (`float("inf")`) if unreachable.
  """

  pos = r, c
  if pos in memo:
    return memo[pos]  # Return cached distance if available

  # Base cases: Out of bounds or revisited (within this recursive call)
  if r < 0 or r >= len(mat) or c < 0 or c >= len(mat[0]) or pos in visited:
    return float("inf")

  if pos in visited:
        return float("inf")  # Return infinity if the position is already visited to avoid cycles

  visited.add(pos)  # Mark the current cell as visited (within this recursive call)

  # If the cell contains 0, it's the base case with distance 0
  if mat[r][c] == 0:
    memo[pos] = 0
    return 0

  # Recursively find the minimum distance in all four directions
  up_distance = 1 + _find_min_distance_to_zero(mat, r+1, c, visited, memo)
  down_distance = 1 + _find_min_distance_to_zero(mat, r-1, c, visited, memo)
  right_distance = 1 + _find_min_distance_to_zero(mat, r, c+1, visited, memo)
  left_distance = 1 + _find_min_distance_to_zero(mat, r, c-1, visited, memo)

  # Find the minimum distance from neighboring cells
  memo[pos]memo[pos] = min(up_distance, down_distance, right_distance, left_distance)  # Store the result in memo
  visited.remove(pos)  # Remove the current position from the visited set to allow other paths to use it
  return memo[pos]

# Time Complexity: O(n * m), where n is the number of rows and m is the number of columns in the matrix.
# Each cell is processed once, and memoization ensures that each cell's result is computed only once.

# Space Complexity: O(n * m) for the memo dictionary to store results for each cell and 
# O(n + m) for the recursion stack in the worst case.

# Further Notes:
# - The use of a visited set for each cell ensures that cycles are avoided during the recursive calls.
# - The memo dictionary stores the minimum distance for each cell, reducing redundant calculations.
# - This approach guarantees that we explore all possible paths from each cell to find the nearest 0 efficiently.


