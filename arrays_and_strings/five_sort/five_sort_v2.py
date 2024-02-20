def five_sort(nums):
    """
    have two pointers at either end; left & right
    while the pointers don't overlap, do:
        -if element at left is 5:
            -check if element at right is 5:
            yes?
                decrement right by one
            no?
                swap right and left values
            decrement right by 1
            increment left by one
        -else:
            -increment left by one
    """
    left = 0
    right = len(nums)-1
    
    while left<=right:
        if nums[left] == 5:
            if nums[right] == 5:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
                left += 1
                
        else:
            left += 1
            
    return nums