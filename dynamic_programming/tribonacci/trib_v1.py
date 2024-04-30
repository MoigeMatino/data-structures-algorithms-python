def tribonacci(n: int) -> int:
    """
    Calculates the nth Tribonacci number using a recursive approach.

    Args:
        n (int): The index of the Tribonacci number to calculate (0-based).

    Returns:
        int: The nth Tribonacci number.

    This function implements a naive recursive approach to calculate the nth Tribonacci number. 
    The Tribonacci sequence is defined as:

      T(n) = T(n-1) + T(n-2) + T(n-3)

    While it's easy to understand, this approach suffers from exponential time complexity 
    (O(3^n)) due to repeated calculations of subproblems. For larger values of n, this can become
    computationally expensive.

    Consider using memoization or iterative approaches for better performance
    when dealing with larger n.
    """

    # Base cases: T(0) = 0, T(1) = 0, T(2) = 1
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1

    # Recursive case: T(n) = T(n-1) + T(n-2) + T(n-3)
    trib_n = tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
    return trib_n

# Time Complexity: O(3^n)
# - Each recursive call calculates the Tribonacci number for three smaller inputs (n-1, n-2, n-3).
# - In the worst case, this leads to a branching tree of function calls, resulting in exponential 
#   complexity (O(3^n)) as the number of function calls grows rapidly with n.

# Space Complexity: O(n)
# - The recursive calls use the call stack, which can grow up to a depth of n recursive calls
#   in the worst case. This results in a space complexity of O(n).

# Approach and Reasoning:
# This function implements a naive recursive approach to calculate the nth Tribonacci number.
# It follows the definition of the Tribonacci sequence:

# T(n) = T(n-1) + T(n-2) + T(n-3), where T(0) = 0, T(1) = 0, and T(2) = 1.

# For each value of n, the function makes three recursive calls: one for T(n-1), another for T(n-2), 
# and a third for T(n-3). However, this approach suffers from a major drawback: redundant calculations.

# Consider the calculation of tribonacci(6). It involves calculating tribonacci(5), which in turn 
# calculates tribonacci(4), tribonacci(3), and so on. The subproblems tribonacci(4), tribonacci(3), etc., 
# are calculated multiple times across different branches of the recursion tree. This redundancy leads 
# to exponential time complexity.

# Note:
# - For larger values of n, the recursive approach becomes computationally expensive due to the
#   repeated calculations.
