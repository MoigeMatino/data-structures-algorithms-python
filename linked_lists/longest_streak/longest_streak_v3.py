def longest_streak(head):
    """
    Finds the length of the longest streak of equal values in a linked list.

    Args:
        head (Node): The head node of the linked list.

    Returns:
        int: The length of the longest streak of equal values.
    """

    current = head  # Initialize current node pointer to the head
    curr_val = head.val  # Store the value of the head node for comparison
    max_streak = 0  # Initialize variable to track the longest streak seen so far
    curr_streak = 0  # Initialize variable to track the current streak

    while current:  # Iterate through the linked list
        if current.val == curr_val:  # Check if current node's value equals the comparison value
            curr_streak += 1        # Increment current streak if values are equal
        else:
            curr_val = current.val  # Update comparison value if values differ
            curr_streak = 1        # Reset current streak for new potential streak

        if curr_streak > max_streak:  # Check if current streak is longer than max streak
            max_streak = curr_streak  # Update max streak if necessary

        current = current.next  # Move current pointer to the next node

    return max_streak  # Return the length of the longest streak

# Time Complexity: O(n)
# The while loop iterates through the linked list once in the worst case (n nodes).
# This results in linear time complexity proportional to the list's length.

# Space Complexity: O(1)
# The function uses constant extra space for variables (max_streak, curr_streak, curr_val),
# independent of the linked list's size. This is considered constant space complexity.
