def remove_node(head, target_val):
    """
    Removes the first node from the linked list that has the specified target value (recursive approach).

    Args:
        head (Node): The head node of the linked list.
        target_val (int): The value to be removed from the list.

    Returns:
        Node: The head node of the modified linked list, potentially with the target node removed.
    """

    if head is None:  # Base case: Empty list, nothing to remove
        return None

    # Check if head node is the target node
    if head.val == target_val:
        return head.next  # Return the next node as the new head

    # Recursively remove the target node from the rest of the list
    head.next = remove_node(head.next, target_val)

    # Return the (potentially modified) head node
    return head

# Time Complexity: O(n)
# In the worst case (target value not found), the function calls itself for each node
# in the linked list, leading to a linear time complexity proportional to the list's length.

# Space Complexity: O(n)
# Due to recursion, the function call stack can grow up to the list's length in the worst case,
# resulting in linear space complexity.

# Notes on Approach and Reasoning:
# This code implements a recursive approach to remove the first occurrence of a target value from a linked list.
# It checks for an empty list as the base case.
# If the head node itself is the target node, it returns the next node as the new head.
# Otherwise, it recursively calls itself on the `head.next` node, passing the same target value.
# The recursive call attempts to remove the target from the remaining list.
# After the recursive call returns, it updates the `head.next` pointer with the modified list (potentially without the target).
# Finally, it returns the (potentially modified) head node.

# This recursive approach is concise but has a higher space complexity due to the call stack compared to the iterative approach.
