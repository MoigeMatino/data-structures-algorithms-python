def longest_streak(head):
    """
    Finds the length of the longest streak of equal values in a linked list.

    Args:
        head (Node): The head node of the linked list.

    Returns:
        int: The length of the longest streak of equal values.
    """

    prev = None  # Initialize variable to store the previous node's value
    max_streak = 0  # Initialize variable to track the longest streak seen so far
    current_streak = 0  # Initialize variable to track the current streak

    current = head  # Initialize current node pointer to the head

    while current is not None:  # Iterate through the linked list
        if current.val == prev:  # Check if current node's value equals previous node's value
            current_streak += 1  # Increment current streak if values are equal
        else:
            current_streak = 1  # Reset current streak if values differ

        prev = current.val  # Update previous node value for next comparison

        if current_streak > max_streak:  # Check if current streak is longer than max streak
            max_streak = current_streak  # Update max streak if necessary

        current = current.next  # Move current pointer to the next node

    return max_streak  # Return the length of the longest streak

# Time Complexity: O(n)
# The while loop iterates through the linked list once in the worst case (n nodes).
# This results in linear time complexity proportional to the list's length.

# Space Complexity: O(1)
# The function uses constant extra space for variables (prev, max_streak, current_streak),
# independent of the linked list's size. This is considered constant space complexity.

# Notes on Approach and Reasoning:
# The code iterates through the linked list. In each iteration:
#   - It compares the current node's value with the previous node's value.
#   - If the values are equal, it increments the current streak.
#   - If the values differ, it resets the current streak to 1.
#   - It updates the previous node's value for the next comparison.
#   - It compares the current streak with the maximum streak and updates the max streak if necessary.
# After iterating through the entire list, the function returns the maximum streak length found.
