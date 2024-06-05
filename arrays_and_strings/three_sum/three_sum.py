from typing import List

def three_sum(nums:List) -> List[List[int]]:
    """
    Finds all unique triplets in the given list that sum to zero.

    Args:
        nums (list[int]): A list of integers.

    Returns:
        list[list[int]]: All unique triplets in the given list that sum to zero.

    This function finds all unique triplets in the given list that sum to zero.
    """
    nums.sort()
    triplets = []

    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        low = i + 1
        high = len(nums) - 1

        while low < high:
            current_sum = nums[i] + nums[low] + nums[high]
            if current_sum == 0:
                triplets.append([nums[i], nums[low], nums[high]])

                while low < high and nums[low] == nums[low+1]:
                    low += 1
                
                while low < high and nums[high] == nums[high-1]:
                    high -= 1

                low += 1
                high -= 1
            elif current_sum < 0:
                low += 1
            else:
                high -= 1

    return triplets
