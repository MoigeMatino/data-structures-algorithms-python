def tribonacci(n: int) -> int:
    """
    Calculates the nth Tribonacci number using memoization to improve performance.

    Args:
        n (int): The index of the Tribonacci number to calculate (0-based).

    Returns:
        int: The nth Tribonacci number.

    This function implements a memoized recursive approach to calculate the nth Tribonacci number.
    It uses a dictionary (`memo`) to store previously calculated results. When a subproblem
    is encountered again, the stored value is retrieved instead of making a redundant recursive
    call. This significantly improves the time complexity compared to the naive recursive approach.
    """

    # Initialize an empty dictionary to store memoized results
    memo = {}
    # Delegate the actual calculation to the helper function
    return _tribonacci(n, memo)

def _tribonacci(n: int, memo: dict[int, int]) -> int:
    """
    Helper function for calculating the nth Tribonacci number using memoization.

    Args:
        n (int): The index of the Tribonacci number to calculate (0-based).
        memo (dict[int, int]): A dictionary to store previously calculated results.

    Returns:
        int: The nth Tribonacci number.
    """

    # Check if the result for n is already stored in the memo
    if n in memo:
        return memo[n]

    # Base cases: T(0) = 0, T(1) = 0, T(2) = 1
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1

    # Calculate the Tribonacci number for n
    trib_n = _tribonacci(n - 1, memo) + _tribonacci(n - 2, memo) + _tribonacci(n - 3, memo)

    # store the Tribonacci number for n in the memo
    memo[n] = trib_n
    return memo[n]

# Time Complexity: O(n)
# - The memoization technique avoids redundant calculations of subproblems.
# - Each subproblem is solved at most once, and the result is stored in the memo.
# - In the worst case, the function makes n recursive calls (one for each Tribonacci number up to n).
#   However, these calls are constant time lookups (for memo access) or calculations for new values.
# - Therefore, the time complexity is considered linear (O(n)).

# Space Complexity: O(n)
# - The memo dictionary stores the results of subproblems, which can grow up to a depth of n
#   recursive calls in the worst case. This results in a space complexity of O(n).

# Approach and Reasoning:
# This approach utilizes memoization to optimize the recursive solution for calculating Tribonacci numbers.
# Memoization is a technique to store the results of subproblems to avoid recomputing them
# if they are encountered again.

# The code defines two functions:

# 1. `tribonacci(n)`: This is the main function that takes the desired index `n` as input. It initializes
#    an empty dictionary (`memo`) and delegates the actual calculation to the helper function `_tribonacci(n, memo)`.
# 2. `_tribonacci(n, memo)`: This helper function performs the memoized recursive calculation. It first checks
#    if the result for `n` is already stored in the `memo` dictionary. If it exists, the stored value is
#    returned directly, avoiding redundant calculations. If the result is not found in the memo, the function
#    makes three recursive calls (for n-1, n-2, and n-3) using itself (`_tribonacci`) and stores the sum
#    (T(n)) in the memo dictionary. Finally, it returns the calculated value T(n).

# By storing previously calculated results in the memo, this approach significantly improves the time
# complexity compared to the naive recursive approach, which suffers from exponential complexity due to
# redundant calculations.
