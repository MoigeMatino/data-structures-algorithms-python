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

    # Helper function to perform the actual knight's move calculation with memoization
    return _knightly_number(n, m, kr, kc, pr, pc, {})


def _knightly_number(n: int, m: int, kr: int, kc: int, pr: int, pc: int, memo: dict) -> int:
    """
    This helper function recursively calculates the number of valid knight's moves
    on an n x n chessboard to reach a target position from a starting position within a given number of moves (m),
    using memoization to avoid redundant calculations.

    Args:
        n (int): The size of the chessboard (n x n).
        m (int): The number of allowed knight's moves.
        kr (int): The starting row index of the knight.
        kc (int): The starting column index of the knight.
        pr (int): The target row index of the knight.
        pc (int): The target column index of the knight.
        memo (dict): A dictionary to store previously calculated results for specific positions and remaining moves.

    Returns:
        int: The number of valid knight's moves to reach the target position from the starting position within m moves.
    """

    # Create a unique key to store the result for the current position and remaining moves in the memoization dictionary
    key = (m, kr, kc)

    # Check if the result for this specific position and remaining moves has already been calculated and memoized
    if key in memo:
        return memo[key]

    # Check if the starting knight position is outside the chessboard boundaries
    if kr < 0 or kr >= n or kc < 0 or kc >= n:
        return 0  # Invalid starting position, return 0

    # Base case: If there are no more moves left (m = 0)
    if m == 0:
        # Check if the knight is at the target position
        if (kr, kc) == (pr, pc):
            return 1  # Reached target position, return 1
        else:
            return 0  # Not at target position with no moves left, return 0

    # Define all possible knight's moves (eight directions)
    neighbors = [
        (kr + 2, kc + 1), 
        (kr - 2, kc + 1), 
        (kr + 2, kc - 1), 
        (kr - 2, kc - 1),
        (kr + 1, kc + 2), 
        (kr - 1, kc + 2), 
        (kr + 1, kc - 2), 
        (kr - 1, kc - 2),
    ]

    # Count the number of valid knight's moves from the current position
    count = 0
    for neighbor in neighbors:
        neighbor_row, neighbor_col = neighbor  # Unpack the potential new row and column positions

        # Check if the new position is within the chessboard boundaries
        if 0 <= neighbor_row < n and 0 <= neighbor_col < n:
            # Recursively explore the number of valid moves from the new position with m-1 moves remaining
            # and update the memo with the result for the new position and remaining moves
            count += _knightly_number(n, m - 1, neighbor_row, neighbor_col, pr, pc, memo)

    # Memoize the result for the current position and remaining moves before returning
    memo[key] = count
    return count

"""
Time Complexity: O(m * n^2)
- The time complexity is determined by the number of moves (m) and the size of the chessboard (n x n).
- For each move, the function explores up to 8 possible neighbor positions, resulting in O(8m) operations.
- Since we're using memoization, each unique position and remaining moves are calculated only once, leading to O(m * n^2).

Space Complexity: O(m * n^2)
- The space complexity is dominated by the memoization dictionary, which can store results for each unique position and remaining moves.
- The maximum number of unique positions is bounded by the number of cells on the chessboard (n x n) multiplied by the number of moves (m).

Approach and Reasoning:
- This algorithm uses dynamic programming with memoization to efficiently calculate the number of valid knight's moves.
- It recursively explores all possible knight's moves from the starting position within the given number of moves.
- Memoization is used to avoid redundant calculations for the same position and remaining moves, optimizing the overall runtime.
- The algorithm defines all possible neighbor positions for a knight's move and recursively explores valid moves from each position.
- By memoizing the results for each unique position and remaining moves, the algorithm avoids recalculating the same subproblems.
- This approach efficiently handles large chessboards and a significant number of allowed moves, making it suitable for practical use cases.
"""
