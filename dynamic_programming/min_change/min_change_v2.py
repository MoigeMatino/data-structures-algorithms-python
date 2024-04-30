def min_change(amount: int, coins: list[int]) -> int:
    """
    Calculates the minimum number of coins required to make a given amount of money using a list of coin denominations.

    Args:
        amount (int): The target amount of money to make change for.
        coins (list[int]): A list of available coin denominations (positive integers).

    Returns:
        int: The minimum number of coins required to make the target amount, or -1 if it's impossible.

    This function implements a memoized recursive approach to determine the minimum number of coins needed
    to make the target amount ('amount') using the provided coin denominations ('coins').
    """

    # Delegate the actual calculation with memoization to the helper function
    ans = _min_change(amount, coins, {})
    # Handle the case where no combination of coins can make the amount
    if ans == float('inf'):
        return -1
    return ans

def _min_change(amount: int, coins: list[int], memo: dict[int, int]) -> int:
    """
    Helper function for calculating the minimum number of coins required to make a given amount.

    Args:
        amount (int): The remaining target amount.
        coins (list[int]): A list of available coin denominations (positive integers).
        memo (dict[int, int]): A dictionary to store memoized results (amount -> minimum coins).

    Returns:
        int: The minimum number of coins required to make the remaining amount, or float('inf') if impossible.
    """

    # Check if the result for this amount is already stored in the memo
    if amount in memo:
        return memo[amount]

    # Base case: If the target amount is 0, no coins are needed (minimum of 0 coins)
    if amount == 0:
        return 0

    # Base case: If the target amount is negative, it's impossible (set minimum coins to infinity)
    if amount < 0:
        return float('inf')

    # Initialize minimum coins to positive infinity (assuming the worst case initially)
    min_coins = float('inf')

    # Try each coin denomination
    for coin in coins:
        # Calculate the number of coins needed for the remaining amount after using the current coin
        remaining_amount = amount - coin
        num_coins = 1 + _min_change(remaining_amount, coins, memo)  # Add 1 for the current coin

        # Update minimum coins if a smaller combination is found
        min_coins = min(min_coins, num_coins)

    # Store the minimum coins for this amount in the memo and return it
    memo[amount] = min_coins
    return memo[amount]

# Time Complexity: O(a * c)
# - The memoization technique avoids redundant calculations of subproblems.
# - Each subproblem (making a specific remaining amount) is solved at most once and stored in the memo.
# - In the worst case, the function explores all possible combinations of coins, leading to a maximum of 'a'
#   (target amount) subproblems and 'c' (number of coin choices) calculations per subproblem. This results
#   in a time complexity of O(a * c).

# Space Complexity: O(a)
# - The memo dictionary stores the results of subproblems, which can grow up to a depth of 'a' (target amount)
#   recursive calls in the worst case. This results in a space complexity of O(a).

# Approach and Reasoning:
# This approach combines memoization with the recursive strategy to solve the minimum coin change problem.
# Memoization is used to store the minimum number of coins needed for different subproblems (making various
# remaining amounts). This significantly reduces redundant calculations and improves efficiency compared to
# the naive recursive approach that would explore all combinations repeatedly.
