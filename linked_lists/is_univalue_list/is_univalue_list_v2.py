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

    if head.next is None:  # Single-node list is a univalue list
        return True

    next_node = head.next  # Store the next node for comparison

    # Check if head and next node have different values (early termination)
    if head.val != next_node.val:
        return False

    # Recursive call to check the remaining list starting from the next node
    return is_univalue_list(next_node)

# Time Complexity: O(n)
# In the worst case, the recursive function calls itself for each node in the linked list
# until the end is reached (n nodes). This results in a linear time complexity.

# Space Complexity: O(n)
# Due to recursion, each function call creates a stack frame on the call stack.
# The depth of the call stack grows with the number of recursive calls, which is proportional 
# to the number of nodes (n) in the worst case. This leads to a space complexity of O(n).

# Notes on Approach and Reasoning:
# This code implements a recursive approach to check if a linked list is a univalue list.
# It handles the empty and single-node list cases as univalue lists for efficiency.
# It then stores the next node for comparison and checks if its value differs from the head's value.
# If the values differ, the list is not a univalue list, and the function returns False.
# Otherwise, it makes a recursive call to check the remaining list starting from the next node.
# This recursive approach is concise but can be less space-efficient for large linked lists.
# The recursive calls create stack frames, and the space complexity grows proportionally to the list's length (n) in the worst case.
# For very large lists, an iterative approach might be preferable due to its constant space complexity. 
# An iterative approach would iterate through the list using a loop, avoiding the function call overhead and stack usage.
