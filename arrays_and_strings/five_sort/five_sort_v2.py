def five_sort(nums: list[int]) -> list[int]:
    """
    Sorts a list of numbers in-place, moving all 5s to the end of the list while preserving
    the relative order of non-5 elements.

    Args:
        nums (list[int]): The list of numbers to sort.

    Returns:
        list[int]: The original list with all 5s moved to the end.
    """

    # Initialize left and right pointers (one at the beginning, one at the end)
    left = 0
    right = len(nums) - 1

    # Loop while the pointers haven't crossed
    while left <= right:
        # Check the element at the left pointer
        if nums[left] == 5:
            # If it's a 5, check the element at the right pointer
            if nums[right] == 5:
                # If the element at right is also a 5, move the right pointer inwards (skip it)
                right -= 1
            else:
                # If the element at right is not a 5, swap them and move both pointers
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1  # Move right pointer inwards (considering swapped element)
                left += 1   # Move left pointer outwards (since the swapped element is now a 5)
        # If the element at left is not a 5, move the left pointer outwards (consider it)
        else:
            left += 1

    # Return the original list with 5s moved to the end (in-place modification)
    return nums

# Time Complexity: O(n)
# The time complexity is linear (O(n)) because the while loop iterates at most n times
# (in the worst case, where all elements need to be checked). In each iteration, a constant
# amount of operations (comparisons, swaps, pointer movements) are performed.

# Space Complexity: O(1)
# The algorithm uses constant extra space for the two pointers (left and right). It modifies the
# original list in-place, so the space complexity remains constant regardless of the input size.

# Approach and Reasoning:
# This algorithm uses a two-pointer technique to sort the list in-place. It maintains two pointers:

#  - `left`: starting from the beginning of the list.
#  - `right`: starting from the end of the list.

# The loop iterates as long as `left` is less than or equal to `right`. It considers two cases for
# the element at `left`:

# 1. If the element at `left` is a 5, we further check the element at `right`:
#    - If the element at `right` is also a 5, we simply decrement `right` to move it inwards
#      (effectively ignoring it for now).
#    - If the element at `right` is not a 5, we swap them and move both pointers. We decrement
#      `right` to consider the swapped element (which is now a 5), and increment `left` to move
#      forward (since the original element at `left` is now effectively placed).
# 2. If the element at `left` is not a 5, we simply increment `left` to consider the next element.

# By repeatedly iterating through these cases, the algorithm partitions the list. Elements less than
# or equal to 5 are effectively placed at the beginning (up to index `left` - 1), and elements equal to 5
# are placed at the end (from index `left` onwards). The original order of non-5 elements is preserved.
