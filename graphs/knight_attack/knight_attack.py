from collections import deque

def knight_attack(board_size, knight_row, knight_col, prey_row, prey_col):
    """
    Finds the minimum number of moves required for a knight to reach its prey on a chessboard.

    Args:
        board_size (int): The size of the square chessboard.
        knight_row (int): The row position of the knight.
        knight_col (int): The column position of the knight.
        prey_row (int): The row position of the prey.
        prey_col (int): The column position of the prey.

    Returns:
        int or None: The minimum number of moves required for the knight to reach the prey, or None if unreachable.
    """
    queue = deque([(knight_row, knight_col, 0)])  # Initialize queue with knight's position and initial moves
    visited = {(knight_row, knight_col)}  # Track visited positions

    while queue:
        r, c, moves = queue.popleft()  # Dequeue the current position and number of moves

        if r == prey_row and c == prey_col:  # Check if the knight reaches the prey
            return moves

        valid_movements = get_valid_movements(board_size, r, c)  # Get valid movements from the current position
        for movement in valid_movements:
            valid_move_r, valid_move_c = movement
            if movement not in visited:
                visited.add(movement)  # Mark the position as visited
                queue.append((valid_move_r, valid_move_c, moves + 1))  # Enqueue the next position with incremented moves

    return None  # Return None if prey is unreachable

def get_knight_moves(board_size, r, c):
    """
    Generates valid knight movements given its current position on the board.

    Args:
        board_size (int): The size of the square chessboard.
        r (int): The current row position of the knight.
        c (int): The current column position of the knight.

    Returns:
        list of tuple: A list of valid movements as tuples (row, column).
    """
    movement_deltas = [
        ( r + 2, c + 1 ),
        ( r - 2, c + 1 ),
        ( r + 2, c - 1 ),
        ( r - 2, c - 1 ),
        ( r + 1, c + 2 ),
        ( r - 1, c + 2 ),
        ( r + 1, c - 2 ),
        ( r - 1, c - 2 ),
    ]
    valid_movements = [];
    for movement in movement_deltas:
        move_r, move_c = movement
        new_r = move_r
        new_c = move_c
        row_inbound = 0 <= new_r < board_size  # Check if the new row is within the board boundaries
        col_inbound = 0 <= new_c < board_size  # Check if the new column is within the board boundaries
        if row_inbound and col_inbound:
            valid_movements.append((new_r, new_c))

    return valid_movements  # Return valid movements
"""

n = length of the board
Time: O(n^2) - because there are n*n possible positions on the grid and we traverse each of those positions at most once.
Space: O(n^2)

FURTHER NOTES
This algorithm employs a breadth-first search (BFS) algorithm to find the minimum number of moves required for a knight piece
to reach its prey on a square chessboard. The algorithm utilizes a queue to explore all possible moves from the knight's current
position, marking visited positions to avoid redundant exploration. The knight_attack function iterates through possible moves until
it finds the prey or exhausts all possibilities. Meanwhile, the get_valid_movements function generates valid knight movements given the
current position on the board. 

WHY BFS?
The Breadth-First Search (BFS) approach is ideal for this problem due to its ability to efficiently find the shortest path from the knight
to its prey on a chessboard. BFS explores all possible moves from the knight's current position level by level, ensuring that the shortest 
path is found first. This is crucial in scenarios where the objective is to minimize the number of moves required to reach the target, as is 
the case in this problem. Additionally, BFS guarantees that if a path exists, it will be found with minimal exploration, making it a suitable 
choice for problems where the search space is relatively small, such as on a chessboard. Furthermore, BFS guarantees optimality in finding the 
shortest path in unweighted graphs, which applies to this problem since each move of the knight is considered to have equal weight. Therefore, 
BFS provides an efficient and optimal solution for finding the minimum number of moves for the knight to reach its prey.

"""
