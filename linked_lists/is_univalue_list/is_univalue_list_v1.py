def is_univalue_list(head):
    """
    Checks if a linked list is a univalue list (all nodes have the same value).

    Args:
        head (Node): The head node of the linked list.

    Returns:
        bool: True if the list is a univalue list, False otherwise.
    """

    if head is None:  # Empty list is considered a univalue list with no value
        return True

    head_val = head.val  # Store the value of the head node

    current = head.next  # Initialize a pointer to the next node

    while current is not None:  # Iterate through the list
        if current.val != head_val:  # Check if current node's value differs from head
            return False
        current = current.next  # Move to the next node

    # If the loop completes without finding a differing value, all nodes have the same value
    return True

# Time Complexity: O(n)
# The `while` loop iterates through each node in the linked list once in the worst case (n nodes).
# This results in a linear time complexity proportional to the number of nodes (n).

# Space Complexity: O(1)
# The function uses constant extra space for pointers (`head`, `current`), and a variable (`head_val`),
# independent of the linked list's size. This is considered constant space complexity.

# Notes on Approach and Reasoning:
# This code implements an iterative approach to check if a linked list is a univalue list.
# It handles the empty list case as a univalue list.
# It stores the value of the head node and iterates through the remaining nodes.
# In each iteration, it compares the current node's value with the head node's value.
# If a differing value is found, the list is not a univalue list, and the function returns False.
# If the loop completes without finding a differing value, all nodes have the same value, 
# and the function returns True.
# This iterative approach is efficient and avoids the overhead associated with recursion for this problem.
