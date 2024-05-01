def count_paths(grid):
    return _count_paths(grid, 0, 0)

def _count_paths(grid, r, c):
    if r == len(grid) or c == len(grid[0]) or grid[r][c] == 'X':
        return 0
    
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return 1
    
    down_paths = _count_paths(grid, r + 1, c)
    right_paths = _count_paths(grid, r, c + 1)

    return down_paths + right_paths