from collections import deque

def best_bridge(grid):
    """
    Finds the shortest distance between two islands on the grid.

    Args:
        grid (List[List[str]]): A 2D grid representing the islands where 'L' represents land and 'W' represents water.

    Returns:
        int: The shortest distance between the two islands.

    """
    # Find the first island for traversal
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            island = find_island(grid, r, c, set())
            if len(island) > 0:
                first_island = island
                break
    
    visited = set(first_island)
    queue = deque([ ])
    for pos in visited:
        r, c = pos
        queue.append((r,c,0))
    # begin BFS traversal
    while queue:
        r, c, distance = queue.popleft()

        # If a land cell is found and it's not part of the first island, return the distance
        if grid[r][c] == "L" and pos not in first_island:
            return distance - 1
        
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for delta in deltas:
            delta_r, delta_c = delta
            neighbor_row = r + delta_r
            neighbor_col = c + delta_c
            neighbor_pos = (neighbor_row, neighbor_col)

            if inbounds(grid, neighbor_row, neighbor_col) and neighbor_pos not in visited:
                visited.add(pos)
                queue.append((neighbor_row, neighbor_col, distance +1))

def inbounds(grid, r, c):
    """
    Checks if a given position is within the bounds of the grid.

    Args:
        grid (List[List[str]]): A 2D grid representing the islands.
        r (int): The row index.
        c (int): The column index.

    Returns:
        bool: True if the position is within the grid bounds, False otherwise.
    """
    row_inbounds = 0 <= r < len(grid)
    col_inbounds = 0 <= c < len(grid[0])
    return row_inbounds and col_inbounds

def find_island(grid, r, c, visited):
    """
    Finds all positions of the island connected to the given position.

    Args:
        grid (List[List[str]]): A 2D grid representing the islands.
        r (int): The row index.
        c (int): The column index.
        visited (set): A set of visited positions.

    Returns:
        set: A set of positions belonging to the island connected to the given position.
    """
    if not inbounds(grid, r, c) or grid[r][c] == 'W':
        return visited
    
    pos = (r,c)

    if pos in visited:
        return visited
    
    visited.add(pos)

    find_island(grid, r - 1, c, visited)
    find_island(grid, r + 1, c, visited)
    find_island(grid, r, c-1, visited)
    find_island(grid, r, c+1, visited)

"""
Time Complexity Analysis:
- Finding the first island: O(r*c), where r is number of rows and c is number of columns in the grid.
- BFS traversal to find the shortest distance between islands: O(e), where e is the number of edges (neighbors) of the islands.
Overall: O(r*c + e)

Space Complexity Analysis:
- Storing visited nodes: O(r*c), where n is the size of the grid.
- Storing nodes being visited: O(r*c).
Overall: O(r*c)

FURTHER NOTES:
This algorithm first finds one island using depth-first search (DFS) traversal. It then performs a breadth-first search (BFS) 
traversal to find the shortest distance between this island and the nearest 'L' (land) cells that are not part of the first island. 
The algorithm iterates through each cell in the grid to find the first island, and then conducts BFS to find the shortest distance 
between the first island and the nearest land cells. This approach efficiently utilizes DFS for island discovery and BFS for distance calculation.
The 'distance - 1' adjustment is made to account for the fact that the BFS traversal starts from the initial island. When the BFS encounters the 
first land cell outside of this island, it calculates the distance from the starting point of the traversal (which is part of the initial island) 
to this land cell. Since the distance represents the number of steps taken in the traversal, subtracting 1 ensures that the returned distance 
corresponds to the distance between the two islands, excluding the starting land cell. Therefore, distance - 1 ensures that the calculated distance 
accurately reflects the shortest distance between the two islands.
"""
