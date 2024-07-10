class Node:
    """
    Represents a node in a singly linked list.

    Attributes:
        val (int): The value stored in the node.
        next (Node): A reference to the next node in the linked list, or None if it's the last node.
    """

    def __init__(self, val):
        """
        Initializes a new Node instance.

        Args:
            val (int): The value to store in the node.
        """
        self.val = val
        self.next = None

def traverse(head):
    """
    Traverses a singly linked list and returns a list of all node values.

    Args:
        head (Node): The head node of the linked list.

    Returns:
        list[int]: A list containing the values of all nodes in the linked list in the order they appear.
    """

    nodes = []  # Create an empty list to store node values
    current = head  # Start at the head node

    while current:  # Loop as long as current is not None
        nodes.append(current.val)  # Append current node's value to the list
        current = current.next  # Move to the next node in the linked list

    return nodes

"""
Time Complexity: O(n)

The `traverse` function iterates through the entire linked list once, where n is the number of nodes. The number of 
times the loop iterates is directly proportional to the number of nodes in the list.

Space Complexity: O(n)

The function creates a new list `nodes` to store the values. The size of this list grows in proportion to the number 
of nodes in the linked list.

"""
