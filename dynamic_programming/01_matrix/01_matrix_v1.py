from collections import deque


def find_min_distance_to_zero(mat: list[list[int]]) -> list[list[int]]:
  """
  Finds the minimum distances to all cells containing the value 0 in a matrix.

  This function takes a 2D matrix represented as a list of lists of integers as input.
  It iterates through the matrix and identifies all cells containing the value 0.
  For each cell with 0, it performs a Breadth-First Search (BFS) to explore neighboring cells.
  The distance to each reachable cell is calculated as the distance from the nearest 0 cell plus 1.
  The distances are stored in a separate matrix of the same dimensions as the input matrix.

  Args:
      mat: A 2D list of integers representing the matrix.

  Returns:
      A 2D list of integers representing the minimum distances to 0 for each cell.
      If a cell is unreachable from any 0 cell, the distance is set to infinity (`float("inf")`).
  """

  rows = len(mat)  # Get the number of rows in the matrix
  cols = len(mat[0])  # Get the number of columns in the matrix

  # Initialize a distances matrix to store minimum distances to 0
  distances = [[float("inf")] * cols for _ in range(rows)]

  # Create a queue to use for BFS exploration
  queue = deque()

  # Find all cells with 0 and mark them as distance 0, enqueue them for exploration
  for r in range(rows):
    for c in range(cols):
      if mat[r][c] == 0:
        distances[r][c] = 0
        queue.append((r, c))

  # Perform BFS exploration from cells with 0
  while queue:
    current_r, current_c = queue.popleft()  # Dequeue the current cell

    # Define potential neighboring cell offsets (up, down, left, right)
    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for delta in deltas:
      delta_r, delta_c = delta  # Unpack the offset

      # Calculate the neighbor's row and column coordinates
      neighbor_r = current_r + delta_r
      neighbor_c = current_c + delta_c

      # Check if the neighbor is within matrix bounds
      row_inbounds = 0 <= neighbor_r < rows
      col_inbounds = 0 <= neighbor_c < cols

      if row_inbounds and col_inbounds:  # If neighbor is within bounds
        if distances[neighbor_r][neighbor_c] > distances[current_r][current_c] + 1:
          # Update distance if it's shorter than the current distance + 1
          distances[neighbor_r][neighbor_c] = distances[current_r][current_c] + 1
          queue.append((neighbor_r, neighbor_c))  # Enqueue neighbor for further exploration

  return distances

# Time Complexity: O(rows * cols) in the worst case.
# The algorithm iterates through the entire matrix once (O(rows * cols)) to
# identify cells with 0 and perform BFS exploration. The BFS itself visits
# each reachable cell at most once, contributing to the overall time complexity.

# Space Complexity: O(rows * cols).
# The algorithm uses two matrices: the input matrix (`mat`) and the distances matrix.
# Both have dimensions `rows * cols`, leading to a space complexity of O(rows * cols).

# Note:
# This approach utilizes Breadth-First Search (BFS) to explore neighboring cells
# from all cells containing 0. BFS ensures that the shortest distances are found
# for all reachable cells. The distances are stored in a separate matrix for efficient
# access and representation of the minimum distances to 0 for each cell in the matrix.
