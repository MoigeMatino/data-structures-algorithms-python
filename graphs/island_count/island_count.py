def island_count(grid):
    """
    Counts the number of islands in the grid.

    Args:
        grid (List[List[str]]): A 2D grid representing the landscape where 'W' represents water and 'L' represents land.

    Returns:
        int: The number of islands in the grid.

    """
    visited = set()  # Set to store visited positions
    count = 0
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid, r, c, visited) == True:  # Explore the grid from each position and increment count if a new island is found
                count += 1
            
    return count

def explore(grid, r, c, visited):
    """
    Explores the grid starting from the given position to identify an island.

    Args:
        grid (List[List[str]]): A 2D grid representing the landscape where 'W' represents water and 'L' represents land.
        r (int): The row index of the starting position.
        c (int): The column index of the starting position.
        visited (set): A set of visited positions.

    Returns:
        bool: True if an island is found, False otherwise.

    """
    row_inbounds = 0 <= r < len(grid)  # Check if the row index is within bounds
    column_inbounds = 0 <= c < len(grid[0])  # Check if the column index is within bounds
    
    if not row_inbounds or not column_inbounds:  # If the position is out of bounds, return False
        return False
    
    if grid[r][c] == 'W':  # If the position is water, return False
        return False
    
    pos = (r,c)
    if pos in visited:  # If the position is already visited, return False
        return False
    
    visited.add(pos)  # Mark the position as visited
    # Recursively explore neighboring positions
    explore(grid, r - 1, c, visited)
    explore(grid, r + 1, c, visited)  
    explore(grid, r, c - 1, visited)
    explore(grid, r, c + 1, visited)
    
    return True  # Return True indicating an island is found

"""
Time Complexity Analysis:
- Exploring each position on the grid: O(rc), where r is the number of rows and c is the number of columns.
Overall: O(rc)

Space Complexity Analysis:
- Storing visited positions: O(rc), where r is the number of rows and c is the number of columns.
Overall: O(rc)

Further Notes:
This algorithm utilizes depth-first search (DFS) to explore the grid and identify islands. It iterates through each position on the grid 
and explores the neighboring positions recursively to determine if an island is present. The count of islands is incremented each time a 
new island is found. The time and space complexities are both O(rc), where r is the number of rows and c is the number of columns in the grid. 
It's important to handle the case where the explore function returns False, indicating that the position represents water, has already been 
visited, or is out of bounds. This ensures that the algorithm correctly counts the islands in the grid.
"""
