def get_node_value(head, index):
    """
    Retrieves the value of a node at a specific index in a linked list using recursion.

    Args:
        head (Node): The head node of the linked list.
        index (int): The index of the node to retrieve the value from.

    Returns:
        int: The value stored in the node at the specified index, or None if the index is invalid.
    """

    if head is None:  # Base case: Empty list or index out of bounds (negative or exceeds length)
        return None

    if index == 0:  # Base case: Target node is the head node
        return head.val

    # Recursive case: Decrement the index and traverse to the next node
    return get_node_value(head.next, index - 1)

# Time Complexity: O(n)
# In the worst case, the recursive function calls itself for each node
# in the linked list until the target index (0) is reached or the end is reached.
# This results in a linear time complexity proportional to the number of nodes (n).

# Space Complexity: O(n)
# Due to recursion, each function call creates a stack frame on the call stack.
# This stack frame stores information about the function call, local variables,
# and the return address. The depth of the call stack grows with the number of
# recursive calls, which can be up to n (number of nodes) in the worst case.
# This leads to a space complexity of O(n).

# Notes on Approach and Reasoning:
# This code implements a recursive approach to retrieve the value at a specific index.
# It checks for base cases: an empty list or the target index being 0 (head node).
# Otherwise, it recursively calls itself with `head.next` and decrements the index.
# This effectively traverses the list until the target index is reached.
# While concise, recursion can be less space-efficient for large linked lists
# due to the overhead of function calls and the call stack usage.
# For very large lists, an iterative approach might be preferable due to its constant space complexity.
