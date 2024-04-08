def reverse_list(head):
    """
    Reverses a linked list iteratively.

    Args:
        head (Node): The head node of the linked list to reverse.

    Returns:
        Node: The new head node of the reversed linked list.
    """

    previous = None  # Initialize a pointer for the previous node
    current = head    # Initialize a pointer for the current node

    while current is not None:  # Iterate through the linked list
        next_node = current.next  # Store the current node's next node

        # Reverse the link: current node now points to the previous node
        current.next = previous

        # Update pointers for the next iteration
        previous = current  # Previous node becomes the current node
        current = next_node  # Move current node to the next stored node

    # After the loop, 'previous' will be pointing to the new head node
    return previous

# Time Complexity: O(n)
# The `while` loop iterates through each node in the linked list once.
# In the worst case, this happens for all n nodes. This results in a linear
# time complexity proportional to the number of nodes (n).

# Space Complexity: O(1)
# The function uses constant extra space for three pointers (`previous`, `current`, and `next_node`),
# independent of the linked list's size. This is considered constant space complexity.

# Notes on Approach and Reasoning:
# This code implements an iterative approach to reverse a linked list.
# It maintains three pointers: `previous`, `current`, and `next_node`.
# The loop iterates through the list, performing the following in each step:
#  1. Store the `current` node's `next` node in `next_node`.
#  2. Reverse the link by setting `current.next` to point to the `previous` node.
#  3. Update the pointers: `previous` becomes the current node, and `current` moves to the `next_node` (stored earlier).
# After the loop completes, the `previous` pointer will be pointing to the new head node
# of the reversed list, which is then returned.
# This iterative approach is generally efficient for reversing linked lists and avoids
# the overhead associated with recursion.
