def island_count(grid):
    visited = set()
    count = 0
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid, r, c, visited) == True:
                count += 1
            
    return count

def explore(grid, r, c, visited):
    row_inbounds = 0 <= r < len(grid)
    column_inbounds = 0 <= c < len(grid[0])
    
    if not row_inbounds or not column_inbounds:
        return False
    
    if grid[r][c] == 'W':
        return False
    
    pos = (r,c)
    if pos in visited:
        return False
    
    visited.add(pos)
    
    explore(grid, r - 1, c, visited)
    explore(grid, r + 1, c, visited)  
    explore(grid, r, c - 1, visited)
    explore(grid, r, c + 1, visited)
    
    return True

"""
A grid is a special representation of a graph. The mode of traversal is different.
The nodes in a grid are represented by its position([row][col]). Hence the gird[r][c]
to get the value of the node at that position.
The grid is traversed in a spiral fashion.

    r = number of rows
    c = number of columns
    Time: O(rc)
    Space: O(rc)

"""