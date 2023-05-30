def count_paths(grid):
    return _count_paths(grid, 0, 0, {})

def _count_paths(grid, r, c, memo):
    pos = (r,c)

    if pos in memo:
        return memo[pos]
    
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 'X':
        return 0
    
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return 1
    
    down_paths = _count_paths(grid, r+1, c, memo)
    right_paths = _count_paths(grid, r, c+1, memo)

    memo[pos] = down_paths + right_paths 

    return memo[pos]

"""
r = # rows
c = # columns
Time: O(r*c)
Space: O(r*c)

"""