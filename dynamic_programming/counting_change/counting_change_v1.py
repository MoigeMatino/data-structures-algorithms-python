def counting_change(amount: int, coins: list[int]) -> int:
    """
    Calculates the number of ways to make a given amount using coins from a list.

    Args:
        amount (int): The target amount to reach.
        coins (list[int]): A list of coin denominations.

    Returns:
        int: The number of unique combinations of coins that sum up to the target amount.

    This function implements a recursive approach to find the number of ways to make a given amount (`amount`)
    using coins from a provided list (`coins`). The function utilizes a helper function (`_counting_change`)
    that performs the core logic.

    - The function calls the helper function with the initial arguments (amount, coins, and an index starting at 0).
    """
    return _counting_change(amount, coins, 0)

def _counting_change(amount: int, coins: list[int], idx: int) -> int:
    """
    Helper function for calculating the number of ways to make change.

    Args:
        amount (int): The remaining target amount.
        coins (list[int]): The list of coin denominations.
        idx (int): The current index in the coins list (used for iteration).

    Returns:
        int: The number of unique combinations of coins that sum up to the remaining amount.

    - Base cases:
        - If the target amount (`amount`) is 0, there's one way to make change (using no coins).
        - If the target amount is negative, there are no ways to make change.

    - Recursive case:
        - The function iterates through each possible quantity (`qty`) of the current coin (`coin`) at the
          current index (`idx`) that can be used without exceeding the target amount.
            - `qty` ranges from 0 to the maximum number of coins of that denomination without exceeding amount
              (amount // coin).
        - Calculate the remaining amount after using `qty` coins of the current denomination.
        - Recursively call `_counting_change` with the remaining amount and the next coin in the list
          (updated index). This explores all possible combinations using the remaining coins.
        - Add the number of ways found from the recursive call to a running total (`total_ways`).

    - Finally, the function returns the total number of ways to make change using coins from the list.
    """

    if amount == 0:
        return 1
    if amount < 0:
        return 0

    coin = coins[idx]
    total_ways = 0

    for qty in range(amount // coin + 1):
        remainder_amount = amount - (qty * coin)
        ways_for_remainder = _counting_change(remainder_amount, coins, idx + 1)
        total_ways += ways_for_remainder

    return total_ways

# where n is the amount and m is the number of coins
# Time Complexity: O(m^n).
# The recursive function iterates through each coin in the list (coins). Let C be the number of coins in the list.
# For each coin, the function explores all possible quantities (qty) of that coin that can be used without exceeding 
# the target amount (amount). In the worst case, it considers using the coin up to amount // coin times. The key point 
# is that this exploration happens independently for each coin. So, there are C branches at each level of the recursion, 
# leading to an exponential growth in the number of possibilities.

# Space Complexity: O(n).
# Due to recursive call stack

# Notes:
# - This algorithm uses recursion to explore all possible combinations of coins.
# - It calculates the number of ways to make change by considering each coin denomination.
# - The function _counting_change is recursive, breaking down the problem into smaller subproblems.
# - The time complexity is polynomial due to the recursive nature, making it suitable for small inputs.
# - However, for larger inputs, it might not be the most efficient solution due to potential stack overflow.
# - Dynamic programming can be applied to improve efficiency for larger inputs.

