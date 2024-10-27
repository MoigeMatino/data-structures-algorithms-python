def max_area(height: list[int]) -> int:
    """
    Calculate the maximum area of water a container can store, formed by two lines
    from the given list of heights and the x-axis.

    Parameters:
    height (list[int]): A list of integers representing the heights of vertical lines.

    Returns:
    int: The maximum area of water that can be contained.

    """
    left = 0
    right = len(height) - 1
    max_area = 0
    
    while left < right:
        # Calculate the height and width of the current container
        curr_height = min(height[left], height[right])
        curr_width = right - left
        curr_area = curr_height * curr_width
        
        # Update max_area if the current area is larger
        max_area = max(curr_area, max_area)
        
        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return max_area

# Approach and Reasoning:
#     -----------------------
#     - We use the two-pointer technique to solve this problem efficiently.
#     - Initialize two pointers, `left` at the start and `right` at the end of the list.
#     - The width of the container is the distance between the two pointers.
#     - The height of the container is determined by the shorter of the two lines at the pointers.
#     - Calculate the area for the current pair of lines and update `max_area` if this area is larger.
#     - Move the pointer pointing to the shorter line inward to potentially find a taller line,
#         which might result in a larger area.
#     - Repeat the process until the two pointers meet.

#     Time Complexity:
#     ----------------
#     - The time complexity of this approach is O(n), where n is the number of elements in the `height` list.
#     - This is because each element is processed at most once as the pointers move towards each other.

#     Space Complexity:
#     -----------------
#     - The space complexity is O(1) because we are using a constant amount of extra space,
#       regardless of the input size.
            