"""
1. Find one island -> traversal dfs
    -iterate through all the nodes on the grid
    -for each node; explore the neighbors not W
    -if neighbor is L:
        =add to visited
    -recursively visit neighbors
2. To find shortest distance between island one and two
    (finding the shortest distance between two nodes) => BF
"""
from collections import deque

def best_bridge(grid):
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
    
    while queue:
        r, c, distance = queue.popleft()

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
    row_inbounds = 0 <= r < len(grid)
    col_inbounds = 0 <= c < len(grid[0])
    return row_inbounds and col_inbounds

def find_island(grid, r, c, visited):
    if not inbounds(grid, r, c) or grid[r][c] == 'W':
        return visited
    
    pos = (r,c)cd

    if pos in visited:
        return visited
    
    visited.add(pos)

    find_island(grid, r - 1, c, visited)
    find_island(grid, r + 1, c, visited)
    find_island(grid, r, c-1, visited)
    find_island(grid, r, c+1, visited)
