def is_univalue_list(head, prev_val=None):
    """
    Checks if a linked list is a univalue list (all nodes have the same value).

    Args:
        head (Node): The head node of the linked list.
        prev_val (int, optional): The value of the previous node (default: None).

    Returns:
        bool: True if the list is a univalue list, False otherwise.
    """

    if head is None:  # Empty list is considered a univalue list with no value
        return True

    # If prev_val is None, it's the first node. Set prev_val to the head's value.
    if prev_val is None:
        prev_val = head.val

    # Check if current node's value matches the previous value
    if head.val == prev_val:
        # Recursive call to check the remaining list with updated prev_val
        return is_univalue_list(head.next, prev_val)
    else:
        # Values differ, not a univalue list
        return False

# Time Complexity: O(n)
# The recursive function calls itself for each node in the linked list, leading to a linear time complexity.

# Space Complexity: O(n)
# Due to recursion, each function call creates a stack frame.
# The depth of the stack frames grows with the number of nodes (n) in the worst case, resulting in O(n) space complexity.

# Notes on Approach and Reasoning:
# This code implements a recursive approach with an optional `prev_val` argument to track the previous node's value.
# It handles empty lists as univalue lists.
# It checks for the first node and sets `prev_val` to the head's value if necessary.
# It compares the current node's value with `prev_val`. If they match, it makes a recursive call with updated `prev_val`.
# If values differ, the list is not univalue, and it returns False.
# This approach efficiently avoids redundant checks for the first node using `prev_val`.
# It's concise but less space-efficient for large lists due to stack frames.
# For very large lists, an iterative approach with a loop might be preferable for constant space complexity.
