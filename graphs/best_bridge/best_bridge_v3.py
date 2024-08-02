from typing import List, Set, Tuple
from collections import deque

def best_bridge(grid: List[List]) -> int:
    visited = set()
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            island = find_island(grid, r, c, visited)
            if len(island) > 0:
                break
        if len(island) > 0:
            first_island = island
            break
        
    if len(island) == 0:
        return "No island in sight"
    
    queue = deque([])
    for pos in first_island:
        r, c = pos
        queue.append((r, c, 0))
        
    newly_visited = set()
    
    while queue:
        curr_r, curr_c, distance = queue.popleft()
        curr_pos = curr_r, curr_c
        
        if grid[curr_r][curr_c] == "L" and curr_pos not in first_island:
            return distance - 1
        
        deltas = deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]  #  Possible directions to move in the grid
        for delta in deltas:
            delta_r, delta_c = delta
            neighbor_r = delta_r + curr_r
            neighbor_c = delta_c + curr_c
            neighbor_pos = neighbor_r, neighbor_c
            if inbounds(grid, neighbor_r, neighbor_c) and neighbor_pos not in newly_visited:
                newly_visited.add(neighbor_pos)
                queue.append((neighbor_r, neighbor_c, distance + 1))
    return -1    


def find_island(grid: List[List], r: int, c: int, visited: Set[Tuple]) -> bool:
    queue = deque([(r,c)])
    
    while queue:
        curr_r, curr_c = queue.popleft()
        curr_pos = curr_r, curr_c
        
        if grid[curr_r][curr_c] == "W" or curr_pos in visited:
            continue
        
        visited.add(curr_pos)
        deltas = deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]  #  Possible directions to move in the grid
        for delta in deltas:
            delta_r, delta_c = delta
            neighbor_r = delta_r + r
            neighbor_c = delta_c + c
            if inbounds(grid, neighbor_r, neighbor_c):
                queue.append((neighbor_r, neighbor_c))
                
    return visited

def inbounds(grid: List[List], r: int, c: int) -> bool:
    row_inbounds = 0 <= r < len(grid)
    col_inbounds = 0 <= c < len(grid[0])

    return row_inbounds and col_inbounds

