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

def create_linked_list(values):
    """
    Creates a linked list from a list of values.

    Args:
        values (list): A list of values to be inserted into the linked list.

    Returns:
        Node: The head node of the created linked list.
    """

    dummy_head = Node(None)  # Create a dummy head node to simplify handling the first element
    tail = dummy_head  # Initialize tail pointer to the dummy head

    for value in values:  # Iterate through the input list of values
        tail.next = Node(value)  # Create a new node for the current value
        tail = tail.next        # Update the tail pointer to the newly created node

    # Return the actual head node (excluding the dummy head)
    return dummy_head.next

# Time Complexity: O(n)
# The for loop iterates through the input list of values once.
# In each iteration, it creates a new node, resulting in linear time complexity proportional to the list's length (n).

# Space Complexity: O(n)
# The function creates n new Node objects, one for each value in the input list.
# This results in linear space complexity proportional to the list's length.

# Notes on Approach and Reasoning:
# This code implements a function to create a linked list from a list of values.
# It creates a dummy head node to simplify handling the first element in the list.
# The `tail` pointer is used to traverse the list during construction.
# The code iterates through the input list of values.
# In each iteration:
#   - It creates a new node with the current value.
#   - It updates the `next` pointer of the current tail node to point to the newly created node.
#   - It updates the `tail` pointer to reference the newly created node for the next iteration.
# After iterating through all values, the function returns the actual head node of the created linked list (excluding the dummy head).
# This approach is efficient and avoids unnecessary checks or modifications to the original input list.
