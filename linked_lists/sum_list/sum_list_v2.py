def sum_list(head):
    """
    Calculates the sum of all values in a linked list using recursion.

    Args:
        head (Node): The head node of the linked list.

    Returns:
        int: The sum of all values in the linked list.
    """

    if head is None:  # Base case: If the list is empty, return 0 (sum of no elements)
        return 0

    # Recursive case: Add the current node's value and the sum of the remaining list
    return head.val + sum_list(head.next)
"""
Time Complexity: O(n)
The recursive function traverses the entire linked list once,
making a call for each node. This results in a linear time complexity
proportional to the number of nodes (n) in the worst-case scenario.

Space Complexity: O(n)
Due to recursion, function calls create a call stack. Each call adds a
stack frame containing information about the call, local variables,
and return addresses. The depth of the stack grows proportionally
to the number of nodes in the linked list, leading to a space complexity
of O(n) in the worst-case scenario.

Notes on Approach and Reasoning:
This code implements a recursive approach to sum the linked list values.
It checks for the base case (empty list) and returns 0 in that case.
Otherwise, it recursively calls itself with the `head.next` node.
The return value from the recursive call (sum of remaining elements)
is added to the current node's value and returned.
While concise, recursion can be less efficient for large linked lists
due to the overhead of function calls and the call stack usage. 
"""
