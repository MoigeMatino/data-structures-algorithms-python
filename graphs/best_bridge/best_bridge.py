from typing import List, Set
from collections import deque

def best_bridge(grid: List[List]) -> int:
    """
    Finds the length of the shortest bridge connecting two islands in a grid.

    Args:
        grid: A 2D list representing the grid, where 'L' represents land and 'W' represents water.

    Returns:
        The length of the shortest bridge, or -1 if no bridge can be found.
    """

    visited = set()  # Set to keep track of visited cells

    for r in range(len(grid)):  # Iterate through each row
        for c in range(len(grid[0])):  # Iterate through each column
            island = find_island(grid, r, c, visited)  # Find an island starting from (r, c)
            if len(island) > 0:  # If an island is found
                break
        if len(island) > 0:  # If an island is found in this row
            first_island = island  # Store the first found island
            break
    if len(island) == 0:  # If no island is found
        return "No island in sight"  # Indicate no island

    queue = deque([])  # Queue for BFS
    for pos in first_island:  # Initialize the queue with the first island's positions
        r, c = pos
        queue.append((r, c, 0))  # Add positions with distance 0 to the queue

    newly_visited = set()  # Set to keep track of newly visited cells in BFS

    while queue:
        r, c, distance = queue.popleft()  # Get the next position and distance from the queue
        pos = r, c

        if grid[r][c] == "L" and pos not in first_island:  # If found the second island
            return distance - 1  # Return the distance minus 1 (since we started at 0)

        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]  #  Possible directions to move in the grid
        for delta in deltas:
            delta_r, delta_c = delta
            neighbor_r = delta_r + r
            neighbor_c = delta_c + c
            neighbor_pos = neighbor_r, neighbor_c
            if inbounds(grid, neighbor_r, neighbor_c) and neighbor_pos not in newly_visited:
                newly_visited.add(neighbor_pos)
                queue.append((neighbor_r, neighbor_c, distance + 1))

    return -1  # No bridge found

def find_island(grid: List[List], r: int, c: int, visited: Set) -> Set:
    """
    Finds an island starting from a given position.

    Args:
        grid: The grid representing the land and water.
        r: The row of the starting position.
        c: The column of the starting position.
        visited: A set to keep track of visited cells.

    Returns:
        A set of positions representing the island.
    """

    if not inbounds(grid, r, c):
        return visited # Return visited if the cell is out of bounds
    
    if grid[r][c] == "W":
        return visited # Return visited if the cell is water
    
    pos = r, c
    if pos in visited:
        return visited # Return visited if the cell has already been visited
    
    visited.add(pos) # Mark the cell as visited

    # Recursively visit neighboring cells
    find_island(grid, r + 1, c, visited)
    find_island(grid, r - 1, c, visited)
    find_island(grid, r, c + 1, visited)
    find_island(grid, r, c - 1, visited)

    return visited

def inbounds(grid: List[List], r: int, c: int) -> bool:
    """
    Checks if a given position is within the grid boundaries.

    Args:
        grid: The grid.
        r: The row.
        c: The column.

    Returns:
        True if the position is in bounds, False otherwise.
    """

    row_inbounds = 0 <= r < len(grid)
    col_inbounds = 0 <= c < len(grid[0])

    return row_inbounds and col_inbounds

"""
Time and Space Complexities:

- Time Complexity: O(r * c) where r is the number of rows and c is the number of columns in the grid. This is because each cell is processed a constant number of times.
- Space Complexity: O(r * c) for the visited set and the queue, as we might need to store all the cells in the worst case.

Further Notes:
- Approach:
    - The algorithm uses Depth-First Search (DFS) to identify the first island.
    - Breadth-First Search (BFS) is then used to find the shortest bridge to another island by traversing water cells.
    - The BFS ensures that the shortest path is found due to its level-wise exploration.
- Reasoning:
    - Starting with DFS helps in identifying all connected cells of the first island.
    - BFS is optimal for finding the shortest path in an unweighted grid, which is why it is used after identifying the first island.
"""
