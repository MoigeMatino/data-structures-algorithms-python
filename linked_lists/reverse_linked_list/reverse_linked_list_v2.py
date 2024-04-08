def reverse_list(head, prev=None):
    """
    Reverses a linked list recursively.

    Args:
        head (Node): The head node of the linked list to reverse.
        prev (Node, optional): The previous node in the reversed list during recursion (default: None).

    Returns:
        Node: The new head node of the reversed linked list.
    """

    if head is None:  # Base case: Empty list or end of recursion (reached the tail)
        return prev

    next_node = head.next  # Store the current node's next node for recursion

    # Reverse the link: current node now points to the previous node
    head.next = prev

    # Recursive call to reverse the remaining list with updated `prev` (current node)
    return reverse_list(next_node, head)  # Pass next node and current node as prev for recursion

# Time Complexity: O(n)
# In the worst case, the recursive function calls itself for each node in the linked list
# until the end is reached. This results in a linear time complexity proportional to
# the number of nodes (n).

# Space Complexity: O(n)
# Due to recursion, each function call creates a stack frame on the call stack.
# This stack frame stores information about the function call, local variables,
# and the return address. The depth of the call stack grows with the number of
# recursive calls, which can be up to n (number of nodes) in the worst case.
# This leads to a space complexity of O(n).

# Notes on Approach and Reasoning:
# This code implements a recursive approach to reverse a linked list.
# It utilizes a base case to handle the empty list or the end of the recursion (reached the tail).
# Within the recursive step, it stores the `next` node of the current node.
# Then, it reverses the link by setting `current.next` to point to the `prev` node (passed from the previous call).
# Finally, it makes a recursive call with the `next` node and the current node as the new `prev` for the next iteration.
# This approach is concise but can be less space-efficient for large linked lists due to the call stack usage. 
# For very large lists, an iterative approach might be preferable due to its constant space complexity.
