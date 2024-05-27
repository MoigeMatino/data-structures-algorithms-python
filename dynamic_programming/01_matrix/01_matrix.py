from collections import deque

def update_matrix(mat: list[list[int]]) -> list[list[int]]:
    rows = len(mat)
    cols = len(mat[0])
    distances = [[float("inf")] * cols for _ in range(rows)]
    queue = deque()

    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 0:
                distances[r][c] = 0
                queue.append((r, c))

    while queue:
        current_r, current_c = queue.popleft()

        deltas = [(1,0), (-1,0),(0,1), (0,-1)]
        for delta in deltas:
            delta_r, delta_c = delta
            neighbor_r = current_r + delta_r
            neighbor_c = current_c + delta_c
            row_inbounds = 0 <= neighbor_r < rows
            col_inbounds = 0 <= neighbor_c < cols
            if row_inbounds and col_inbounds:
                if distances[neighbor_r][neighbor_c] > distances[current_r][current_c]:
                    distances[neighbor_r][neighbor_c] = distances[current_r][current_c] + 1
                    queue.append((neighbor_r, neighbor_c))

    return distances



