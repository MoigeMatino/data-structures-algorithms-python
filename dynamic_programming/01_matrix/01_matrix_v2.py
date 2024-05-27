from typing import List, Dict, Set, Tuple, Union
def find_min_distance_to_zero(mat:List[List[int]]) -> Dict[Tuple[int,int],int]:
    rows = len(mat)
    cols = len(mat[0])
    memo = {}
    for r in range(rows):
        for c in range(cols):
            visited = set()
            _find_min_distance_to_zero(mat, r, c, visited, memo)

    return memo

def _find_min_distance_to_zero(mat:List[List[int]], r:int, c:int, visited:Set, memo:Dict[Tuple[int,int],int]) -> Union[int, float]:
    pos = r, c
    if pos in memo:
        return memo[pos]
    
    if r < 0 or r >= len(mat) or c < 0 or c >= len(mat[0]):
        return float("inf")
    
    if pos in visited:
        return float("inf")
    
    visited.add(pos)

    if mat[r][c] == 0:
        memo[pos] = 0
        return 0
    
    up_distance = 1 + _find_min_distance_to_zero(mat, r+1, c, memo, visited)
    down_distance = 1 + _find_min_distance_to_zero(mat, r-1, c, memo, visited)
    right_distance = 1 + _find_min_distance_to_zero(mat, r, c+1, memo, visited)
    left_distance = 1 + _find_min_distance_to_zero(mat, r, c-1, memo, visited)

    memo[pos] = min(up_distance, down_distance, right_distance, left_distance)
    visited.remove(pos)
    return memo[pos]

