def knightly_number(n: int, m: int, kr: int, kc: int, pr: int, pc: int) -> int:
    """
    This function counts the number of valid knight's moves on an n x n chessboard
    to reach a target position from a starting position within a given number of moves (m).

    Args:
        n (int): The size of the chessboard (n x n).
        m (int): The number of allowed knight's moves.
        kr (int): The starting row index of the knight.
        kc (int): The starting column index of the knight.
        pr (int): The target row index of the knight.
        pc (int): The target column index of the knight.

    Returns:
        int: The number of valid knight's moves to reach the target position from the starting position within m moves.
    """

    # Check if the starting knight position is outside the chessboard boundaries
    if kr < 0 or kr >= n or kc < 0 or kc >= n:
        return 0  # Invalid starting position, return 0

    # Base case: If there are no more moves left (m = 0)
    if m == 0:
        # Check if the knight is at the target position
        if kr == pr and kc == pc:
            return 1  # Reached target position, return 1
        else:
            return 0  # Not at target position with no moves left, return 0

    # Define all possible knight's moves (eight directions)
    movements = [
        (kr + 1, kc + 2), 
        (kr + 1, kc - 2), 
        (kr - 1, kc + 2), 
        (kr - 1, kc - 2),
        (kr + 2, kc + 1), 
        (kr + 2, kc - 1), 
        (kr - 2, kc + 1), 
        (kr - 2, kc - 1),
    ]

    # Count the number of valid knight's moves from the current position
    count = 0
    for movement in movements:
        pos_r, pos_c = movement  # Unpack the potential new row and column positions

        # Check if the new position is within the chessboard boundaries
        if 0 <= pos_r < n and 0 <= pos_c < n:
            # Recursively explore the number of valid moves from the new position with m-1 moves remaining
            count += knightly_number(n, m - 1, pos_r, pos_c, pr, pc)

    return count

# Time Complexity: O(n^2 * m) in the worst case
# The time complexity of this algorithm can be O(n^2 * m) in the worst case. This is because for each position on the chessboard 
# (n^2 possibilities) and for each number of moves remaining (m), we explore all eight possible knight's moves. However, in practice, 
# the complexity can be better due to pruning (not exploring invalid positions or positions visited before) and the fact that many 
# positions might not lead to the target within m moves.

# Space Complexity: O(m)
# The space complexity of this algorithm is O(m) due to the recursion call stack. In the worst case, the recursion can go up to a 
# depth of m (number of moves), leading to O(m) space complexity.

# Approach and Reasoning:
# This algorithm uses a recursive backtracking approach to solve the knight's move problem. It starts at the given starting position and 
# explores all possible knight's moves for the remaining number of moves (m). For each move, it checks if the new position is valid (within the 
# chessboard boundaries) and then recursively explores the number of valid moves from that new position with one less move remaining. The final 
# count is the sum of valid moves explored from all possible moves at the starting position.
