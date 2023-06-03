from collections import deque

def knight_attack(n, kr, kc, pr, pc):
    visited = set();
    visited.add((kr, kc))
    queue = deque([ (kr, kc, 0) ])
    while len(queue) > 0:
        r, c, step = queue.popleft();
        if (r, c) == (pr, pc):
            return step
        neighbors = get_knight_moves(n, r, c)
        for neighbor in neighbors:
            neighbor_row, neighbor_col = neighbor
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor_row, neighbor_col, step + 1))
    return None

def get_knight_moves(n, r, c):
    position_deltas = [
        ( r + 2, c + 1 ),
        ( r - 2, c + 1 ),
        ( r + 2, c - 1 ),
        ( r - 2, c - 1 ),
        ( r + 1, c + 2 ),
        ( r - 1, c + 2 ),
        ( r + 1, c - 2 ),
        ( r - 1, c - 2 ),
    ]
    inbounds_positions = [];
    for pos in position_deltas:
        new_row, new_col = pos
        if 0 <= new_row < n and 0 <= new_col < n:
            inbounds_positions.append(pos)
    return inbounds_positions
"""

n = length of the board
Time: O(n^2) - because there are n*n possible positions on the grid and we traverse each of those positions at most once.
Space: O(n^2)

"""
