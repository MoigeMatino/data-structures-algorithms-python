from typing import List, Set
from collections import deque

def best_bridge(grid:List[List]) -> int:
    visited = set()

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            island = find_island(grid, r, c, visited)
            if len(island) > 0:
                break
        if len(island) > 0:
            first_island = island
            print(first_island)
            break
    if len(island) == 0:
        return "No island in sight"
    
    queue = deque([])
    for pos in first_island:
        r, c = pos
        queue.append((r, c, 0))

    newly_visited = set()
    
    while queue:
        r, c, distance = queue.popleft()
        pos = r, c
		
        if grid[r][c] == "L" and pos not in first_island:
            return distance - 1
        
        deltas = [(1,0), (-1,0), (0,1), (0, -1)]
        for delta in deltas:
            delta_r, delta_c = delta
            neighbor_r = delta_r + r
            neighbor_c = delta_c + c
            neighbor_pos = neighbor_r, neighbor_c
            if inbounds(grid, neighbor_r, neighbor_c) and neighbor_pos not in newly_visited:
                newly_visited.add(neighbor_pos)
                queue.append((neighbor_r, neighbor_c, distance+1))

    return -1


def find_island(grid:List[List], r:int, c:int, visited:Set) -> Set:
    if not inbounds(grid, r, c):
        return visited
    
    if grid[r][c] == "W":
        return visited
    
    pos = r, c
    if pos in visited:
        return visited
    
    visited.add(pos)

    find_island(grid, r+1, c, visited)
    find_island(grid, r-1, c, visited)
    find_island(grid, r, c+1, visited)
    find_island(grid, r, c-1, visited)

    return visited

def inbounds(grid:List[List], r:int, c:int) -> bool:
    row_inbounds = 0 <= r < len(grid)
    col_inbounds = 0 <= c < len(grid[0])

    return row_inbounds and col_inbounds
