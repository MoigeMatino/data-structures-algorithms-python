def search_rotated_sorted_array(nums: list[int], low: int, high: int, target: int) -> int:
    """
    Search for a target value in a rotated sorted array using a modified binary search.

    Parameters:
    nums (list[int]): The rotated sorted array.
    low (int): The starting index of the search range.
    high (int): The ending index of the search range.
    target (int): The target value to search for.

    Returns:
    int: True if the target is found, False otherwise.

    """
    if low >= high:
        return False
    
    mid = low + (high - low) // 2
    
    if nums[mid] == target:
        return True
    
    # Check if the left half is sorted
    if nums[low] <= nums[mid]:
        # If target is in the sorted left half
        if nums[low] <= target <= nums[mid]:
            return search_rotated_sorted_array(nums, low, mid - 1, target)
        else:
            return search_rotated_sorted_array(nums, mid + 1, high, target)
    else:
        # If target is in the sorted right half
        if nums[mid] <= target <= nums[high]:
            return search_rotated_sorted_array(nums, mid + 1, high, target)
        else:
            return search_rotated_sorted_array(nums, low, mid - 1, target)
        
# Approach and Rationale:
#     -----------------------
#     - The function uses a recursive binary search approach to find the target in a rotated sorted array.
#     - A rotated sorted array is an array that was originally sorted in increasing order but then rotated at some pivot.
#     - The key observation is that at least one half of the array (either left or right of the midpoint) is always sorted.
#     - By comparing the target with the elements in the sorted half, we can decide which half to continue searching in.
#     - This approach reduces the search space by half in each recursive call, similar to binary search.

#     Time Complexity:
#     ----------------
#     - The time complexity is O(log n), where n is the number of elements in the array.
#     - This is because the search space is halved in each recursive call, similar to binary search.

#     Space Complexity:
#     -----------------
#     - The space complexity is O(log n) due to the recursive call stack.
#     - Each recursive call adds a new layer to the call stack, and the maximum depth of recursion is proportional to log n.
