def max_path_sum(grid):
    return _max_path_sum(grid, 0, 0)

def _max_path_sum(grid, r, c):
    if r == len(grid) or c == len(grid[0]):
        return float("-inf")
    
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return grid[r][c]
    
    down_path_sum = _max_path_sum(grid, r+1, c)
    right_path_sum = _max_path_sum(grid, r, c+1)

    return grid[r][c] + max(right_path_sum, down_path_sum)