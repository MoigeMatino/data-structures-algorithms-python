def counting_change(amount: int, coins: list[int]) -> int:
    """
    Finds the number of ways to make a given amount using a set of coin denominations.

    Args:
        amount (int): The target amount to reach.
        coins (list[int]): A list of coin denominations (positive integers).

    Returns:
        int: The number of distinct ways to make the target amount using the given coin denominations.    
    """

    return _counting_change(amount, coins, 0, {})  # Delegate the calculation to the helper function

def _counting_change(amount: int, coins: list[int], i: int, memo: dict[tuple[int, int], int]) -> int:
    """
    Helper function for calculating the number of ways to make a given amount using coins.

    Args:
        amount (int): The remaining amount to reach.
        coins (list[int]): A list of coin denominations.
        i (int): The current index in the coin list.
        memo (dict[tuple[int, int], int]): A dictionary to store memoized results (amount, coin_index -> number of ways).

    Returns:
        int: The number of distinct ways to make the remaining amount using the remaining coins.
    """

    # Create a unique key for the memo based on remaining amount and current coin index
    key = (amount, i)

    # Check if the number of ways for this amount and coin combination is already stored in the memo
    if key in memo:
        return memo[key]

    # Base case 1: Reached the target amount (successful combination)
    if amount == 0:
        return 1  # One way to make 0 amount: using no coins

    # Base case 2: No more coins left (no valid combination possible)
    if i == len(coins):
        return 0  # No ways to make the amount with no remaining coins

    # Initialize total ways to 0
    total_ways = 0

    # Explore different quantities of the current coin denomination (from 0 to max possible)
    coin = coins[i]
    for qty in range(0, amount // coin + 1):
        # Calculate remaining amount after using the current coin `qty` times
        remainder = amount - (qty * coin)

        # Recursively find the number of ways to make the remaining amount using remaining coins
        ways_for_remainder = _counting_change(remainder, coins, i + 1, memo)

        # Add the number of ways using the current coin `qty` times to the total
        total_ways += ways_for_remainder

    # Store the number of ways for this amount and coin combination in the memo and return it
    memo[key] = total_ways
    return total_ways

# Time Complexity: O(amount * coins)
# - The function explores different quantities of each coin, leading to a loop for each coin.
# - In the worst case, it investigates all possible combinations, resulting in O(amount) for
#   each coin, leading to an overall complexity of O(amount * coins).

# Space Complexity: O(amount * coins)
# - The memoization dictionary can store the number of ways for each unique combination of remaining amount
#   and coin considered up to a

# Approach and reasoning
# This algorithm implements a memoized recursive approach to find the number of ways to make a given amount
# using a set of coin denominations. It explores all possible combinations of coins that can sum up to
# the target amount.

# The algorithm utilizes memoization to store previously computed results in a dictionary (`memo`). This
# avoids redundant calculations for subproblems with the same amount and the same coin considered up to a certain
# point. The `key` used for the memo is a tuple containing the remaining amount and the current coin index.

# The function iterates through each coin denomination and explores different quantities of that coin that
# could be used (from 0 to the maximum possible that can contribute to the remaining amount). For each
# quantity, it recursively calculates the number of ways to make the remaining amount using the remaining
# coins (excluding the current coin used in this iteration). The total number of ways is the sum of these
# combinations for all possible quantities of the current coin.
