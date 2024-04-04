def linked_list_find(head, target):
    """
    Searches a linked list for a specific target value.

    Args:
        head (Node): The head node of the linked list.
        target (int): The value to search for in the linked list.

    Returns:
        bool: True if the target value is found, False otherwise.
    """

    current = head  # Initialize a pointer to the head node

    while current is not None:  # Iterate through the linked list
        if current.val == target:  # Check if current node's value matches the target
            return True  # Target found, return True

        current = current.next  # Move to the next node in the list

    return False  # Reached the end without finding the target, return False

# Time Complexity: O(n)
# The `while` loop iterates through each node in the linked list in the worst case.
# This results in a linear time complexity proportional to the number of nodes (n).

# Space Complexity: O(1)
# The function uses constant extra space for the `current` pointer,
# independent of the linked list's size. This is considered constant space complexity.

# Notes on Approach and Reasoning:
# This code utilizes an iterative approach to search for the target value within the linked list.
# It starts with a pointer (`current`) referencing the head node.
# A `while` loop iterates through the list as long as `current` is not None.
# Inside the loop, the current node's value is compared to the target value.
# If a match is found, the function immediately returns True.
# If the loop completes without finding a match, it returns False, indicating the target wasn't present.
