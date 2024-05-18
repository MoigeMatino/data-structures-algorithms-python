def non_adjacent_sum(nums: list[int]) -> int:
    """
    Calculates the maximum non-adjacent sum of a list of numbers.

    Args:
        nums (list[int]): A list of integers.

    Returns:
        int: The maximum non-adjacent sum of the list.

    This function implements a recursive approach to find the maximum sum of a non-adjacent subsequence
    in a given list of numbers. It considers two possibilities at each element:

    1. Include the current element: Add the current element's value to the maximum non-adjacent sum obtained
       by considering elements from two positions ahead (excluding the next element).
    2. Exclude the current element: Consider the maximum non-adjacent sum obtained by keeping elements
       from the next position onwards (excluding the current element).

    The function returns the maximum of these two possibilities, effectively choosing the scenario
    (include or exclude) that leads to a higher non-adjacent sum.
    
    """
    # Base case: if the list is empty, return 0
    if len(nums) == 0:
        return 0
    
    # Recursive case 1: include the first element and sum with the result of the list excluding the next element
    include = nums[0] + non_adjacent_sum(nums[2:])
    
    # Recursive case 2: exclude the first element and compute the result for the rest of the list
    exclude = non_adjacent_sum(nums[1:])
    
    # Return the maximum of the two cases
    return max(include, exclude)



# Time Complexity:
# The time complexity of this algorithm is O(2^n), where n is the number of elements in the list. This is because each element 
# leads to two recursive calls (including or excluding the element), resulting in an exponential number of calls.

# Space Complexity:
# The space complexity is O(n) due to the recursion stack. In the worst case, the maximum depth of the recursion stack will be n.

# Further Notes:

# Approach and Reasoning:
# 1. The algorithm uses a recursive approach to find the maximum sum of non-adjacent elements in the list.
# 2. For each element, it considers two scenarios: including the element in the sum (skipping the next element) and excluding the element from the sum.
# 3. Base case is defined to handle an empty list, which returns 0.
# 4. The result for each recursive call is the maximum sum obtained from the two scenarios (including or excluding the current element).

# This naive recursive approach can be highly inefficient for larger lists due to redundant calculations. 
