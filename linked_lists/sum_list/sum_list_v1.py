class Node:  # Assuming this class definition exists elsewhere
    """
    This class represents a node in a linked list.

    Attributes:
        val (int): The value stored in the node.
        next (Node): A reference to the next node in the linked list, or None if it's the last node.
    """
    # ... Node class implementation (if not already provided)

def sum_list(head):
    """
    Calculates the sum of all values in a linked list.

    Args:
        head (Node): The head node of the linked list.

    Returns:
        int: The sum of all values in the linked list.
    """

    sum = 0  # Initialize a variable to store the running sum

    while head is not None:  # Iterate through the linked list as long as head is not None
        sum += head.val  # Add the current node's value to the sum
        head = head.next  # Move to the next node in the linked list

    return sum  # Return the calculated sum

"""
Time Complexity: O(n)
The while loop iterates through each node in the linked list once,
resulting in a linear time complexity in the number of nodes (n).

Space Complexity: O(1)
The function uses constant extra space for the `sum` variable,
independent of the linked list's size. This is considered constant space complexity.

Notes on Approach and Reasoning:
This code utilizes a simple iterative approach to traverse the linked list.
It starts with an empty sum variable and iterates through each node using a `while` loop.
Within the loop, the current node's value is added to the `sum` variable.
Finally, after iterating through all nodes, the accumulated sum is returned.
This approach avoids recursion and is generally more efficient for larger linked lists.
"""
