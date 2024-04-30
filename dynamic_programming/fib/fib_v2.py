def fib(n: int) -> int:
    """
    Calculates the nth Fibonacci number using memoization to improve performance.

    Args:
        n (int): The index of the Fibonacci number to calculate (0-based).

    Returns:
        int: The nth Fibonacci number.

    This function implements a memoized recursive approach to calculate the nth Fibonacci number.
    It uses a dictionary (`memo`) to store previously calculated results. When a subproblem
    is encountered again, the stored value is retrieved instead of making a redundant recursive
    call. This significantly improves the time complexity compared to the naive recursive approach.
    """

    # Initialize an empty dictionary to store memoized results
    memo = {}
    # Delegate the actual calculation to the helper function
    return _fib(n, memo)

def _fib(n: int, memo: dict[int, int]) -> int:
    """
    Helper function for calculating the nth Fibonacci number using memoization.

    Args:
        n (int): The index of the Fibonacci number to calculate (0-based).
        memo (dict[int, int]): A dictionary to store previously calculated results.

    Returns:
        int: The nth Fibonacci number.
    """

    # Base cases: f(0) = 0 and f(1) = 1
    if n == 0 or n == 1:
        return n

    # Check if the result for n is already stored in the memo
    if n in memo:
        return memo[n]

    # Calculate the Fibonacci number for n 
    fib_n =  _fib(n - 1, memo) + _fib(n - 2, memo)

    # store the Fibonacci number for n in the memo
    memo[n] = fib_n
    return memo[n]

# Time Complexity: O(n)
# - The memoization technique avoids redundant calculations of subproblems.
# - Each subproblem is solved at most once, and the result is stored in the memo.
# - In the worst case, the function makes n recursive calls (one for each Fibonacci number up to n).
#   However, these calls are constant time lookups (for memo access) or calculations for new values.
# - Therefore, the time complexity is considered linear (O(n)).

# Space Complexity: O(n)
# - The memo dictionary stores the results of subproblems, which can grow up to a depth of n
#   recursive calls in the worst case. This results in a space complexity of O(n).

# Approach and Reasoning:
# This approach utilizes memoization to optimize the recursive solution for calculating Fibonacci numbers.
# Memoization is a technique to store the results of subproblems to avoid recomputing them
# if they are encountered again.

# The code defines two functions:

# 1. `fib(n)`: This is the main function that takes the desired index `n` as input. It initializes
#    an empty dictionary (`memo`) and delegates the actual calculation to the helper function `_fib(n, memo)`.
# 2. `_fib(n, memo)`: This helper function performs the memoized recursive calculation. It first checks
#    the base cases (f(0) and f(1)). Then, it checks if the result for `n` is already stored in the `memo`
#    dictionary. If it exists, the stored value is returned directly, avoiding redundant calculations.
#    If the result is not found in the memo, the function calculates f(n-1) and f(n-2) recursively (using
#    the helper function again) and stores the sum (f(n)) in the memo dictionary. Finally, it returns the
#    calculated value f(n).

# By storing previously calculated results in the memo, this approach significantly improves the time
# complexity compared to the naive recursive approach, which suffers from exponential complexity due to
# redundant calculations.

# Note:
# - Memoization is a powerful technique for optimizing recursive functions with overlapping subproblems.
# - While the space complexity remains O(n) due to the memo dictionary, the significant improvement
#   in time complexity makes this approach suitable for calculating Fibonacci numbers for larger values of n.
