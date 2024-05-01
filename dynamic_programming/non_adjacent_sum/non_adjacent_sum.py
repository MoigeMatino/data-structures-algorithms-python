def non_adjacent_sum(nums: list[int]) -> int:
    """
    Finds the maximum sum of a non-adjacent subset of elements in a given list.

    Args:
        nums (list[int]): A list of integers.

    Returns:
        int: The maximum sum of a non-adjacent subset of elements in the list.

    This function implements a memoized recursive strategy to find the maximum non-adjacent sum.
    A non-adjacent subset means no two elements can be chosen if they are directly next to each other
    in the original list. The function explores two possibilities at each index:

    - Include the current element: Add the current element's value to the maximum non-adjacent sum
      starting from two elements ahead (to avoid including adjacent elements).
    - Exclude the current element: Move on to the next element and consider the maximum non-adjacent sum
      starting from that point.

    The function memoizes the results using a dictionary (`memo`) to avoid redundant calculations.
    """

    return _non_adjacent_sum(nums, 0, {})  # Delegate the calculation to the helper function

def _non_adjacent_sum(nums: list[int], i: int, memo: dict[int, int]) -> int:
    """
    Helper function for calculating the maximum non-adjacent sum, starting from a specific index.

    Args:
        nums (list[int]): A list of integers.
        i (int): The current index in the list.
        memo (dict[int, int]): A dictionary to store memoized results (index -> maximum non-adjacent sum).

    Returns:
        int: The maximum non-adjacent sum starting from the current index.
    """

    # Check if the maximum non-adjacent sum starting from this index is already stored in the memo
    if i in memo:
        return memo[i]

    # Base case: Reached the end of the list
    if i >= len(nums):
        return 0  # No elements to consider, return 0 sum

    # Explore two possibilities: include or exclude the current element
    include = nums[i] + _non_adjacent_sum(nums, i + 2, memo)  # Include + max sum starting from 2 elements ahead
    exclude = _non_adjacent_sum(nums, i + 1, memo)  # Exclude + max sum starting from next element

    # Store the maximum sum from this index in the memo and return it
    memo[i] = max(include, exclude)
    return memo[i]

# Time Complexity: O(n)
# - The recursive function explores at most two possibilities (include or exclude) from each index.
# - In the worst case, all elements are considered, leading to a maximum of 'n' recursive calls.
# - Memoization ensures each element is visited only once, avoiding redundant calculations.
# - Therefore, the time complexity is dominated by the number of elements (n) and is considered linear.

# Space Complexity: O(n)
# - The memoization dictionary (`memo`) stores the maximum non-adjacent sum for each index in the list.
# - In the worst case, the dictionary can hold entries for all 'n' elements.
# - Assuming constant space for the key (index) and value (sum), the space complexity is O(n).

# Approach and Reasoning:
# - This algorithm leverages memoization, a technique to store previously computed results and retrieve
#   them efficiently when encountered again. This avoids redundant calculations for subproblems.
# - The recursive approach breaks down the problem into smaller subproblems (finding the maximum non-adjacent
#   sum starting from each index). At each index, it explores the two possibilities of including or excluding
#   the current element, and memoizes the maximum sum for that subproblem to prevent redundant calculations.