def non_adjacent_sum(nums: list[int]) ->int:
    """
    Calculates the maximum non-adjacent sum of a list of numbers.

    Args:
        nums (list[int]): A list of integers.

    Returns:
        int: The maximum non-adjacent sum of the list.
    """
    if len(nums) == 0:
        return 0
    
    include = nums[0] + non_adjacent_sum(nums[2:])
    exclude = non_adjacent_sum(nums[1:])
    return max(include, exclude)
