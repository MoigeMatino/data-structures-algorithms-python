def longest_streak(head):
    """
    Finds the length of the longest streak of equal values in a linked list.

    Args:
        head (Node): The head node of the linked list.

    Returns:
        int: The length of the longest streak of equal values.
    """

    if head is None:  # Check for empty linked list
        return 0  # Return 0 for empty list (no streaks)

    max_streak = 0  # Initialize variable to track the longest streak seen so far
    current_streak = 1  # Initialize variable to track the current streak
    comparison_val = head.val  # Store the value of the head node for comparison

    current = head.next  # Initialize current node pointer to the second node

    while current is not None:  # Iterate through the linked list (starting from second node)
        if current.val == comparison_val:  # Check if current node's value equals the comparison value
            current_streak += 1  # Increment current streak if values are equal
        else:
            current_streak = 1  # Reset current streak if values differ
            comparison_val = current.val  # Update comparison value for next streak

        if current_streak > max_streak:  # Check if current streak is longer than max streak
            max_streak = current_streak  # Update max streak if necessary

        current = current.next  # Move current pointer to the next node

    # Handle the last node (potential streak ending at the end)
    max_streak = max(max_streak, current_streak)  # Compare final current streak with max streak

    return max_streak  # Return the length of the longest streak

# Time Complexity: O(n)
# The while loop iterates through the linked list once in the worst case (n nodes).
# This results in linear time complexity proportional to the list's length.

# Space Complexity: O(1)
# The function uses constant extra space for variables (max_streak, current_streak, comparison_val),
# independent of the linked list's size. This is considered constant space complexity.

# Notes on Approach and Reasoning:
# This code implements a single-pass iterative approach to find the longest streak of equal values in a linked list.
# It initializes variables to track the maximum streak, the current streak, and the value to compare with subsequent nodes.
# The code iterates through the linked list starting from the second node (since the head node is already considered).
# In each iteration:
#   - It compares the current node's value with the comparison value.
#   - If the values are equal, it increments the current streak.
#   - If the values differ, it resets the current streak and updates the comparison value for the next streak.
#   - It compares the current streak with the maximum streak and updates the max streak if necessary.
# After iterating through the entire list, it compares the final current streak with the max streak
# (to account for potential streaks ending at the last node) before returning the final result.
