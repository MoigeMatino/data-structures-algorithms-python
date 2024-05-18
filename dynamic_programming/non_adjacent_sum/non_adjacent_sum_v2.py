def non_adjacent_sum(nums: list[int]) -> int:
    """
    Calculates the maximum non-adjacent sum of a list of numbers.

    Args:
        nums (list[int]): A list of integers.

    Returns:
        int: The maximum non-adjacent sum of the list.

     This function implements a recursive approach (helper function `_non_adjacent_sum`) to find
    the maximum sum of a non-adjacent subsequence in a given list. It considers two cases at each index:

    1. Include the current element: Add the current element's value to the maximum non-adjacent sum obtained
       by considering elements from two positions ahead (excluding the next element).
    2. Exclude the current element: Consider the maximum non-adjacent sum obtained by keeping elements
       from the next position onwards (excluding the current element).

    The function returns the maximum of these two possibilities, effectively choosing the scenario
    (include or exclude) that leads to a higher non-adjacent sum.
    """
    # Start traversing the list from the first element (index 0)
    return _non_adjacent_sum(nums, 0)


def _non_adjacent_sum(nums: list[int], idx: int) -> int:
    """
    Helper function to recursively calculate the maximum non-adjacent sum starting from a given index.

    Args:
        nums (list[int]): A list of integers.
        idx (int): Current index in the list.

    Returns:
        int: The maximum non-adjacent sum starting from the given index.

    - Base Case:
        - If the index (`idx`) is out of bounds (greater than or equal to the length of the list),
          return 0 (no more elements to consider).

    - Recursive Cases:
        - Include the current element: Add the current element's value (`nums[idx]`) to the
          maximum non-adjacent sum obtained by considering elements from two positions ahead
          (using `idx + 2` to skip the next element).
        - Exclude the current element: Consider the maximum non-adjacent sum obtained by keeping elements
          from the next position onwards (using `idx + 1`).

    - Return the maximum of the two possibilities (include or exclude).
    """
    # Base case: if the current index is out of bounds, return 0
    if idx >= len(nums):
        return 0
    
    # Recursive case 1: include the current element and move to the element after the next one
    include = nums[idx] + _non_adjacent_sum(nums, idx + 2)
    
    # Recursive case 2: exclude the current element and move to the next element
    exclude = _non_adjacent_sum(nums, idx + 1)

    # Return the maximum of the two cases
    return max(include, exclude)


# Time Complexity:
# The time complexity of this algorithm is O(2^n), where n is the number of elements in the list. This is because each element can lead 
# to two recursive calls (including or excluding the element), resulting in an exponential number of calls.

# Space Complexity:
# The space complexity is O(n) due to the recursion stack. In the worst case, the maximum depth of the recursion stack will be n.

# Further Notes:

# Approach and Reasoning:
# 1. The algorithm uses a recursive approach to find the maximum sum of non-adjacent elements in the list.
# 2. For each element, it considers two scenarios: including the element in the sum (skipping the next element) and excluding the element from the sum.
# 3. Base case handles the scenario where the current index is out of bounds, which returns 0.
# 4. The result for each recursive call is the maximum sum obtained from the two scenarios (including or excluding the current element).

# This naive recursive approach can be highly inefficient for larger lists due to redundant calculations. 
