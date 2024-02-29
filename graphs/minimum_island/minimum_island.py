def minimum_island(grid):
    """
    Finds the size of the smallest island in the grid.

    Args:
        grid (List[List[str]]): A 2D grid representing the landscape where 'W' represents water and 'L' represents land.

    Returns:
        int: The size of the smallest island in the grid.

    """
    visited = set()  # Set to store visited positions
    min_size = float("inf")  # Initialize minimum island size to infinity
    size = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = explore_grid(grid, r, c, visited)  # Explore the grid starting from each position
            if size > 0 and size < min_size:  # Update the minimum island size if a non-zero and smaller size is found
                min_size = size
    return min_size

def explore_grid(grid, r, c, visited):
    """
    Explores the grid starting from the given position to find the size of the connected island.

    Args:
        grid (List[List[str]]): A 2D grid representing the landscape where 'W' represents water and 'L' represents land.
        r (int): The row index of the starting position.
        c (int): The column index of the starting position.
        visited (set): A set of visited positions.

    Returns:
        int: The size of the island connected to the starting position.

    """
    row_inbounds = 0 <= r < len(grid)  # Check if the row index is within bounds
    col_inbounds = 0 <= c < len(grid[0])  # Check if the column index is within bounds
    
    if not row_inbounds or not col_inbounds:  # If the position is out of bounds, return size 0
        return 0
    
    if grid[r][c] == "W":  # If the position is water, return size 0
        return 0
    
    pos = (r,c)
    if pos in visited:  # If the position is already visited, return size 0
        return 0
    
    visited.add(pos)  # Mark the position as visited
    size = 1  # Initialize island size to 1
    # Recursively explore neighboring positions and update the island size
    size += explore_grid(grid, r-1, c, visited)
    size += explore_grid(grid, r+1, c, visited)
    size += explore_grid(grid, r, c-1, visited)
    size += explore_grid(grid, r, c+1, visited)
    
    return size

"""
Time Complexity Analysis:
- Exploring each position on the grid: O(rc), where r is the number of rows and c is the number of columns.
Overall: O(rc)

Space Complexity Analysis:
- Storing visited positions: O(rc), where r is the number of rows and c is the number of columns.
Overall: O(rc)

Further Notes:
This algorithm utilizes depth-first search (DFS) to explore the grid and find the size of the connected islands. 
It iterates through each position on the grid and explores the neighboring positions recursively to determine 
the size of the island connected to each position. The minimum island size is tracked and updated accordingly. 
The time and space complexities are both O(rc), where r is the number of rows and c is the number of columns in the grid.
It's important to handle the case where the explore_grid function returns 0, indicating that the position represents water, 
has already been visited, or is out of bounds. This ensures that the algorithm correctly identifies the smallest island size.
"""
