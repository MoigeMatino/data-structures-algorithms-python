def remove_nth_last_node(head, n):
    """
    Removes the nth node from the end of a singly linked list.

    This function uses a two-pointer technique to efficiently remove the nth node from the end of the list.
    The right pointer is advanced by n nodes first, and then both pointers are moved together until the right
    pointer reaches the end of the list. This positions the left pointer just before the node to be removed.

    Args:
        head: The head node of the singly linked list.
        n: The position from the end of the list of the node to be removed.

    Returns:
        The head of the modified linked list with the nth node from the end removed.
    """
    right = head  # Initialize the right pointer to the head of the list
    left = head   # Initialize the left pointer to the head of the list

    # Move the right pointer n steps ahead
    for _ in range(n):
        right = right.next

    # Move both pointers until the right pointer reaches the end of the list
    while right.next is not None:
        right = right.next
        left = left.next

    # Remove the nth node from the end by skipping it
    left.next = left.next.next

    return head

# Time Complexity: O(L)
# The algorithm runs in linear time, where L is the length of the linked list. It involves a single pass
# through the list to advance the right pointer by n steps and another pass to reach the end of the list.

# Space Complexity: O(1)
# The algorithm uses a constant amount of extra space. It only uses a few pointer variables and does not require
# any additional data structures that depend on the size of the input list.

# Approach:
# 1. Use two pointers, right and left, both starting at the head of the list.
# 2. Advance the right pointer by n steps to create a gap of n nodes between the right and left pointers.
# 3. Move both pointers together until the right pointer reaches the end of the list.
# 4. The left pointer will be just before the node to be removed. Adjust the pointers to skip the nth node from the end.
# This approach efficiently removes the nth node from the end in a single pass after the initial setup.