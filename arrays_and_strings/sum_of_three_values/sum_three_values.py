from typing import List, Boolean

def find_sum_of_three(nums:List[int], target:int) -> Boolean:
    """
    Finds if there are three numbers in the given list that sum to the target sum.

    Args:
        nums (list[int]): A list of integers.
        target (int): The target sum to find.

    Returns:
        bool: True if there are three numbers in the given list that sum to the target sum,
              False otherwise.
    """
    nums.sort()

    for i in range(len(nums) - 2):
        low = i + 1
        high = len(nums) - 1

        while low < high:
            current_sum = nums[i] + nums[low] + nums[high]
            if current_sum == target:
                return True
            elif current_sum < target:
                low += 1
            else:
                high -= 1
    return False
