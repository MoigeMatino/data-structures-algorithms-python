from collections import deque

def closest_carrot(grid, starting_row, starting_col):
    visited = {(starting_row, starting_col)}
    queue = deque([ (starting_row, starting_col, 0) ])
    
    while queue:
        row,col,distance = queue.popleft()
        
        if grid[row][col] == "C":
            return distance
        
        deltas = [(1,0),(-1,0),(0,1),(0,-1)]
        
        for delta_row, delta_col in deltas:
            neighbor_row = row + delta_row
            neighbor_col = col + delta_col
            row_inbounds = 0 <= neighbor_row < len(grid)
            col_inbounds = 0 <= neighbor_col < len(grid[0])
            pos = (neighbor_row, neighbor_col)
            if row_inbounds and col_inbounds and pos not in visited and grid[neighbor_row][neighbor_col] != "X":
                visited.add(pos)
                queue.append((neighbor_row, neighbor_col, distance + 1))  
            
    return -1

"""
breadth first is the most effective strategy because it explores all directions evenly at once.

r = number of rows
c = number of columns
Time: O(rc)
Space: O(rc)

"""