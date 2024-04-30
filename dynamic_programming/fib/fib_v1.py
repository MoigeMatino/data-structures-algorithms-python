def fib(n: int) -> int:
    """
    Calculates the nth Fibonacci number using a recursive approach.

    Args:
        n (int): The index of the Fibonacci number to calculate (0-based).

    Returns:
        int: The nth Fibonacci number.

    This function implements a recursive approach to calculate the nth Fibonacci number.
    While it's easy to understand, it suffers from exponential time complexity (O(2^n))
    due to repeated calculations of subproblems. 
    """

    # Base cases: f(0) = 0 and f(1) = 1
    if n == 0 or n == 1:
        return n

    # Recursive case: f(n) = f(n-1) + f(n-2)
    fib_n = fib(n - 1) + fib(n - 2)

    # Return the nth fib number
    return fib_n

# Time Complexity: O(2^n)
# - Each recursive call calculates the Fibonacci number for a smaller input (n-1 and n-2).
# - In the worst case, this leads to a branching tree of function calls, resulting in
#   exponential complexity (O(2^n)) as the number of function calls grows rapidly with n.

# Space Complexity: O(n)
# - The recursive calls use the call stack, which can grow up to a depth of n recursive calls
#   in the worst case. This results in a space complexity of O(n).

# Approach and Reasoning:
# This function implements a naive recursive approach to calculate the nth Fibonacci number.
# It follows the definition of the Fibonacci sequence:

# f(n) = f(n-1) + f(n-2), where f(0) = 0 and f(1) = 1.

# For each value of n, the function makes two recursive calls: one for f(n-1) and another for f(n-2).
# However, this approach suffers from a major drawback: redundant calculations.

# Consider the calculation of fib(6). It involves calculating fib(5), which in turn calculates
# fib(4), fib(3), and so on. The subproblems fib(4), fib(3), etc., are calculated multiple times
# across different branches of the recursion tree. This redundancy leads to exponential time complexity.

# Note:
# - For larger values of n, the recursive approach becomes computationally expensive due to the
#   repeated calculations.
# - V2 implements memoization which is better for performance when dealing with larger n.
#   This approach stores previously calculated results and avoid redundant computations.
