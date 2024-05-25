def find_max_knapsack_profit(capacity: int, weights: list[int], values: list[int]) -> int:
    """
    This function calculates the maximum profit achievable by filling a knapsack with items
    of varying weights and values, subject to a weight capacity limit.

    Args:
        capacity (int): The maximum weight the knapsack can hold.
        weights (list[int]): A list representing the weight of each item.
        values (list[int]): A list representing the value of each item.

    Returns:
        int: The maximum profit achievable by filling the knapsack.
    """

    # Memoization dictionary to store previously computed results for subproblems
    memo = {}

    # Call the helper function to perform the knapsack calculation with memoization
    return _find_max_knapsack_profit(capacity, weights, values, 0, memo)


def _find_max_knapsack_profit(capacity: int, weights: list[int], values: list[int], idx: int, memo: dict) -> int:
    """
    This helper function recursively explores all possible combinations of items
    to find the maximum profit achievable within the knapsack's weight limit, using memoization
    to avoid redundant calculations.

    Args:
        capacity (int): The remaining weight capacity of the knapsack.
        weights (list[int]): A list representing the weight of each item.
        values (list[int]): A list representing the value of each item.
        idx (int): The current index in the items list.
        memo (dict): A dictionary to store previously computed results for subproblems
                    (keyed by remaining capacity and current item index).

    Returns:
        int: The maximum profit achievable considering the current state of the knapsack.
    """

    # Create a unique key for the current subproblem (capacity and item index)
    key = (idx, capacity)

    # Check if the result for this subproblem is already memoized
    if key in memo:
        return memo[key]

    # Base cases:
    # 1. No more capacity or items left: No profit possible (return 0)
    if capacity == 0 or idx == len(weights):
        return 0

    # Get the weight of the current item
    current_weight = weights[idx]

    # Check if the current item can fit in the remaining capacity
    if current_weight <= capacity:
        # Two options:
        #   1. Include the current item:
        #       - Add its value to the maximum profit achievable with the remaining capacity
        #         after including the item's weight.
        include_current = values[idx] + _find_max_knapsack_profit(capacity - current_weight, weights, values, idx + 1, memo)

        #   2. Exclude the current item:
        #       - Consider the maximum profit achievable with the remaining capacity
        #         without including the current item.
        exclude_current = _find_max_knapsack_profit(capacity, weights, values, idx + 1, memo)

        # Store the maximum profit for this subproblem in the memo dictionary
        memo[key] = max(include_current, exclude_current)
        return memo[key]

    else:
        # If the current item is too heavy, exclude it and move to the next item
        memo[key] = _find_max_knapsack_profit(capacity, weights, values, idx + 1, memo)
        return memo[key]


# Time Complexity: O(n * W) in the worst case
# n is the number of items and W is the knapsack capacity. The recursive calls explore all
# possible combinations of items, potentially leading to this complexity. Memoization helps
# reduce redundant calculations significantly.

# Space Complexity: O(n * W) in the worst case
# The space complexity is due to the memoization dictionary that stores intermediate results
# for subproblems. In the worst case, the dictionary might hold entries for all possible
# combinations of items and remaining capacities.

# Approach and Reasoning:
# This algorithm employs a recursive top-down approach with memoization to solve the 0/1
# knapsack problem. It considers two options at each item: include it or exclude it. The
# maximum profit is calculated by recursively exploring both options and choosing the one
# that leads to the highest profit. Memoization is used to store previously computed
# results for subproblems (combinations of remaining capacity and
