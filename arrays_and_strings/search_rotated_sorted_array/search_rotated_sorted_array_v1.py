def search_rotated_sorted_array(nums: list[int], target: int) -> int:
    """
    Search for a target value in a rotated sorted array using an iterative binary search.

    Parameters:
    nums (list[int]): The rotated sorted array.
    target (int): The target value to search for.

    Returns:
    int: The index of the target if found, otherwise -1.

    """
    low = 0
    high = len(nums) - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        # Check if the mid element is the target
        if nums[mid] == target:
            return mid
        
        # Determine if the left half is sorted
        if nums[low] <= nums[mid]:
            # Check if the target is in the sorted left half
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            # Check if the target is in the sorted right half
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    
    # Target not found
    return -1

# Approach and Rationale:
#     -----------------------
#     - This function uses an iterative binary search approach to find the target in a rotated sorted array.
#     - A rotated sorted array is an array that was originally sorted in increasing order but then rotated at some pivot.
#     - The key observation is that at least one half of the array (either left or right of the midpoint) is always sorted.
#     - By comparing the target with the elements in the sorted half, we can decide which half to continue searching in.
#     - This approach reduces the search space by half in each iteration, similar to binary search.

#     Time Complexity:
#     ----------------
#     - The time complexity is O(log n), where n is the number of elements in the array.
#     - This is because the search space is halved in each iteration, similar to binary search.

#     Space Complexity:
#     -----------------
#     - The space complexity is O(1) because the algorithm uses a constant amount of extra space.
