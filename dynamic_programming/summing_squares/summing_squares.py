import math

def summing_squares(n: int) -> int:
    """
    Finds the minimum number of perfect squares that sum up to a given positive integer.

    Args:
        n (int): A positive integer.

    Returns:
        int: The minimum number of perfect squares that sum up to n, or None if no such combination exists.

    """

    return _summing_squares(n, {})  # Delegate the calculation to the helper function

def _summing_squares(n: int, memo: dict[int, int]) -> int:
    """
    Helper function for calculating the minimum number of perfect squares to sum up to a given integer.

    Args:
        n (int): A positive integer.
        memo (dict[int, int]): A dictionary to store memoized results (integer -> minimum number of squares).

    Returns:
        int: The minimum number of perfect squares that sum up to n, or None if no such combination exists.
    """

    # Check if the minimum number of squares for this value of n is already stored in the memo
    if n in memo:
        return memo[n]

    # Base case: If n is 0, no squares are needed (sum is already 0)
    if n == 0:
        return 0

    # Initialize minimum squares with positive infinity (worst-case scenario)
    min_squares = float('inf')

    # Explore all possible perfect squares up to the square root of n
    for i in range(1, int(math.sqrt(n)) + 1):
        # Calculate the current perfect square value (i^2)
        square = i * i

        # Recursively find the minimum number of squares needed for the remaining sum (n - square)
        num_squares = 1 + _summing_squares(n - square, memo)  # Add 1 for the current square

        # Update the minimum squares if a smaller combination is found
        min_squares = min(min_squares, num_squares)

    # Store the minimum number of squares for this value of n in the memo and return it
    memo[n] = min_squares
    return min_squares

# Time Complexity: O(n * sqrt(n))
# - The function iterates through all possible perfect squares up to the square root of n (nested loop).
# - In the worst case, it explores all combinations for each value of n, leading to O(sqrt(n)) for each n.
# - As n increases, the number of iterations grows, resulting in an overall time complexity of O(n * sqrt(n)).

# Space Complexity: O(n)
# - The memoization dictionary (`memo`) stores the minimum number of squares for each encountered value of n.
# - In the worst case, the dictionary can hold entries for all values of n up to a certain limit.
# - Assuming constant space for the key (integer) and value (integer), the space complexity is dominated
#   by the number of entries, resulting in O(n).

# Approach and Reasoning:
# - This algorithm leverages memoization to store previously computed results and avoid redundant work.
# - It utilizes a recursive approach to explore all possible combinations of perfect squares, but stores
#   the minimum number of squares found for each value of n in a memo dictionary.
# - By checking the memo first, the function avoids unnecessary calculations for subproblems that have already been computed

# Further notes:
# This function implements a memoized recursive approach to find the minimum number of perfect squares
# needed to sum up to a given positive integer `n`. A perfect square is an integer that can be obtained
# by squaring an integer. For example, 4 (2^2) and 9 (3^2) are perfect squares.

# The function explores all possible combinations of perfect squares up to the square root of `n`.
# For each perfect square `i^2`, it recursively calculates the minimum number of perfect squares needed
# to sum up to `n - i^2` (remaining sum after subtracting the current perfect square). The function
# keeps track of the minimum number of squares found so far and updates it if a smaller combination is found.

# Memoization is used to store previously computed results in a dictionary (`memo`) to avoid redundant
# calculations. When encountering the same value of `n` again, the stored minimum number of squares is
# retrieved directly from the memo, saving time.
