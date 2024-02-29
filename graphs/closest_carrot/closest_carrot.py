from collections import deque

def closest_carrot(grid, starting_row, starting_col):
    """
    Finds the shortest distance from the starting position to the nearest carrot.

    Args:
        grid (List[List[str]]): A 2D grid representing the landscape where 'C' represents a carrot and 'X' represents an obstacle.
        starting_row (int): The row index of the starting position.
        starting_col (int): The column index of the starting position.

    Returns:
        int: The shortest distance from the starting position to the nearest carrot, or -1 if no carrot is reachable.

    """
    visited = {(starting_row, starting_col)}  # Set to store visited positions
    queue = deque([ (starting_row, starting_col, 0) ])  # Initialize queue with the starting position and distance
    
    while queue:
        row, col, distance = queue.popleft()  # Dequeue a position and its distance
        
        if grid[row][col] == "C":  # If a carrot is found at the current position, return the distance
            return distance
        
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Define possible movements
        
        for delta_row, delta_col in deltas:
            neighbor_row = row + delta_row  # Calculate the row index of the neighboring position
            neighbor_col = col + delta_col  # Calculate the column index of the neighboring position
            row_inbounds = 0 <= neighbor_row < len(grid)  # Check if the neighboring row index is within bounds
            col_inbounds = 0 <= neighbor_col < len(grid[0])  # Check if the neighboring column index is within bounds
            pos = (neighbor_row, neighbor_col)  # Create a tuple representing the neighboring position
            
            # Check if the neighboring position is within bounds, not visited, and not an obstacle
            if row_inbounds and col_inbounds and pos not in visited and grid[neighbor_row][neighbor_col] != "X":
                visited.add(pos)  # Mark the neighboring position as visited
                queue.append((neighbor_row, neighbor_col, distance + 1))  # Enqueue the neighboring position with updated distance
            
    return -1  # Return -1 if no carrot is reachable

"""
Time Complexity Analysis:
- Exploring each position on the grid: O(rc), where r is the number of rows and c is the number of columns.
Overall: O(rc)

Space Complexity Analysis:
- Storing visited positions: O(rc), where r is the number of rows and c is the number of columns.
- Storing positions in the queue: O(rc), where r is the number of rows and c is the number of columns.
Overall: O(rc)

FURTHER NOTES:
The Breadth-First Search (BFS) algorithm is employed here because it efficiently explores all directions evenly at once, 
making it suitable for finding the shortest path to the nearest carrot. The algorithm starts from the given starting 
position and explores neighboring positions in all four directions (up, down, left, and right) until a carrot is found. 
If a carrot is encountered, the algorithm returns the distance to it. Otherwise, if no carrot is reachable, it returns -1. 
The time and space complexities are both O(rc), where r is the number of rows and c is the number of columns in the grid.
"""
