def search_rotated_sorted_array(nums: list[int],low: int, high: int, target:int) -> int:
    
    if low >= high:
        return False
    
    mid = low + (high - low)//2
    
    if nums[mid] == target:
        return True
    
    if nums[low] <= nums[mid]:
        if nums[low] <= target and target <= nums[mid]:
            return search_rotated_sorted_array(nums, low, mid-1, target)
        else:
            return search_rotated_sorted_array(nums, mid+1, high, target)
    else:
        if nums[mid] <= target and target <= nums[high]:
            return search_rotated_sorted_array(nums, mid+1, high, target)
        else:
            return search_rotated_sorted_array(nums, low, mid-1, target)