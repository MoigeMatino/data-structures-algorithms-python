def five_sort(nums: list[int]) -> list[int]:
    """
    Sorts a list of numbers in-place, moving all 5s to the end of the list.

    Args:
        nums (list[int]): The list of numbers to sort.

    Returns:
        list[int]: The original list with all 5s moved to the end, preserving the order of non-5 elements.
    """

    # Initialize two pointers: i (starting from the beginning) and j (starting from the end)
    i = 0
    j = len(nums) - 1

    # Loop while the pointers haven't crossed
    while i <= j:
        # Check the element at j (end)
        if nums[j] == 5:
            # If it's a 5, move the pointer j inwards (towards the beginning)
            j -= 1
        # Check the element at i (beginning)
        elif nums[i] == 5:
            # If it's a 5, swap it with the element at j (which shouldn't be a 5 anymore)
            # and move pointer i forward (since the swapped element is now a 5)
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        # If the element at i is not a 5, move the pointer i forward (considering it)
        else:
            i += 1

    # Return the original list with 5s moved to the end (in-place modification)
    return nums

# Time Complexity: O(n)
# The time complexity is linear (O(n)) because the while loop iterates at most n times
# (in the worst case, where all elements need to be checked). In each iteration, a constant
# amount of operations (comparisons, swaps, pointer movements) are performed.

# Space Complexity: O(1)
# The algorithm uses constant extra space for the two pointers (i and j). It modifies the
# original list in-place, so the space complexity remains constant regardless of the input size.

# Approach and Reasoning:
# This algorithm uses a two-pointer technique to sort the list in-place. It maintains two pointers:
#  - `i`: starting from the beginning of the list.
#  - `j`: starting from the end of the list.

# The loop iterates as long as `i` is less than or equal to `j`. It considers three cases for the elements
# pointed to by `i` and `j`:

# 1. If the element at `j` (end) is a 5, we simply decrement `j` to move it towards the beginning
#    (effectively ignoring it for now).
# 2. If the element at `i` (beginning) is a 5, we swap it with the element at `j` (which shouldn't be a 5
#    at this point) and then increment `i` to move forward (since the swapped element is now a 5).
# 3. If the element at `i` is not a 5, we simply increment `i` to consider the next element.

# By repeatedly iterating through these cases, the algorithm partitions the list. Elements less than
# or equal to 5 are effectively placed at the beginning (up to index `i` - 1), and elements equal to 5
# are placed at the end (from index `i` onwards). The original order of non-5 elements is preserved.
