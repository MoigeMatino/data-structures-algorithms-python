class Node:
    """
    Represents a node in a linked list.

    Attributes:
        val (int): The value stored in the node.
        next (Node): The reference to the next node in the linked list, or None if it's the tail.
    """

    def __init__(self, val):
        """
        Initializes a new Node object.

        Args:
            val (int): The value to be stored in the node.
        """
        self.val = val
        self.next = None

def create_linked_list(values, index=0):
    """
    Creates a linked list from a list of values using recursion.

    Args:
        values (list): A list of values to be inserted into the linked list.
        index (int, optional): Internal index for recursive calls (default: 0).

    Returns:
        Node: The head node of the created linked list, or None if the input list is empty.
    """

    if index == len(values):  # Base case: Reached the end of the input list
        return None

    head = Node(values[index])  # Create a node for the current value
    head.next = create_linked_list(values, index + 1)  # Recursive call to create the rest of the list

    return head

# Time Complexity: O(n)
# The function makes recursive calls until it reaches the end of the input list (base case).
# In each call, it creates a new node, leading to a total of n node creations for n elements in the list.
# This results in linear time complexity proportional to the list's length.

# Space Complexity: O(n)
# Due to recursion, the function call stack can grow up to the list's length in the worst case.
# Each call in the stack holds references to local variables and return addresses, contributing to linear space complexity.

# Notes on Approach and Reasoning:
# This code implements a recursive approach to create a linked list from a list of values.
# It defines a base case for when the index reaches the end of the input list (index == len(values)).
# In each recursive call:
#   - It creates a new node with the current value from the input list at the specified index.
#   - It makes a recursive call to `create_linked_list` with an incremented index to create the remaining nodes.
#   - The recursive call returns the head node of the sub-list created further down the recursion stack.
#   - The current node's `next` pointer is set to reference the head node returned by the recursive call, building the linked structure.
# Finally, the function returns the head node of the entire linked list created from the input values.

# This recursive approach is concise but might have higher space complexity due to the call stack compared to an iterative approach. 
