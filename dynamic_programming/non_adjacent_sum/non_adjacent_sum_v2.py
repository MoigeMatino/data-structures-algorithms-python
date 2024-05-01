def non_adjacent_sum(nums:list[int]) -> int:
    return _non_adjacent_sum(nums, 0) # we start at index zero to start traversing the list from the first element
def _non_adjacent_sum(nums: list[int], idx:int) ->int:
    """
    Calculates the maximum non-adjacent sum of a list of numbers.

    Args:
        nums (list[int]): A list of integers.

    Returns:
        int: The maximum non-adjacent sum of the list.
    """
    if idx == len(nums): # because of off by one errors that could be cause by incrementing the idx by 2, we also need to check if idx could be greater than the length of the nums list
        return 0
    
    include = nums[idx] + _non_adjacent_sum(nums, idx+2)
    exclude = _non_adjacent_sum(nums, idx+1)

    return max(include, exclude)