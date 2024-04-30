def sum_possible(amount: int, numbers: list[int]) -> bool:
    """
    Checks if a given target amount can be formed using any combination of numbers from a list.

    Args:
        amount (int): The target amount to achieve.
        numbers (list[int]): A list of integers representing the available numbers.

    Returns:
        bool: True if the target amount can be formed using the numbers, False otherwise.

    This function implements a memoized recursive approach to determine if the target amount ('amount')
    can be formed using any combination of numbers from the provided list ('numbers').
    
    """

    # Delegate the actual calculation with memoization to the helper function
    return _sum_possible(amount, numbers, {})

def _sum_possible(amount: int, numbers: list[int], memo: dict[int, bool]) -> bool:
    """
    Helper function for checking if a target amount can be formed using any combination of numbers from a list.

    Args:
        amount (int): The remaining target amount.
        numbers (list[int]): A list of integers representing the available numbers.
        memo (dict[int, bool]): A dictionary to store memoized results (amount -> possibility).

    Returns:
        bool: True if the target amount can be formed using the numbers, False otherwise.
    """

    # Check if the result for this amount is already stored in the memo
    if amount in memo:
        return memo[amount]

    # Base case: If the target amount is 0, a valid combination is found (empty sum)
    if amount == 0:
        return True

    # Base case: If the target amount is negative, no valid combination exists
    if amount < 0:
        return False

    # Try each number in the list
    for num in numbers:
        # Check if the remaining amount can be formed using the remaining numbers
        remaining_amount = amount - num
        if _sum_possible(remaining_amount, numbers, memo):
            # If a combination is found for the remaining amount, store the result and return True
            memo[amount] = True
            return True

    # If none of the numbers led to a solution, store False in the memo and return False
    memo[amount] = False
    return memo[amount]

# Time Complexity: O(a * n)
# - The memoization technique avoids redundant calculations of subproblems.
# - Each subproblem (reaching a specific remaining amount) is solved at most once and stored in the memo.
# - In the worst case, the function explores all possible combinations, leading to a maximum of 'a' (target amount)
#   subproblems and 'n' (number of choices) calculations per subproblem. This results in a time complexity of O(a * n).

# Space Complexity: O(a)
# - The memo dictionary stores the results of subproblems, which can grow up to a depth of 'a' (target amount)
#   recursive calls in the worst case. This results in a space complexity of O(a).

# Approach and Reasoning:
#**Memoization:**
    # This approach utilizes memoization to optimize the brute-force recursive solution. It stores previously
    # computed results in a dictionary ('memo') to avoid redundant calculations. When a subproblem
    # (reaching a specific remaining amount) is encountered again, the stored value is retrieved instead of
    # making another recursive call. This significantly improves the time complexity compared to the naive
    # brute-force approach.
# This approach combines memoization with the recursive strategy from the brute-force solution. It leverages
# memoization to store intermediate results (whether a specific remaining amount can be formed) and avoid
# redundant calculations. This significantly improves the time complexity compared to the naive brute-force
# approach, which would explore all combinations repeatedly.
