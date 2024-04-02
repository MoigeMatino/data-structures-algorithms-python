class Node:
    """
    This class represents a node in a linked list.

    Attributes:
        val (int): The value stored in the node.
        next (Node): A reference to the next node in the linked list, or None if it's the last node.
    """

    def __init__(self, val):
        """
        Initializes a new Node object.

        Args:
            val (int): The value to store in the node.
        """
        self.val = val
        self.next = None  # Initially, the next node points to None

def node_values(head):
    """
    Extracts the values of all nodes in a linked list into a list.

    Args:
        head (Node): The head node of the linked list.

    Returns:
        list: A list containing the values of all nodes in the linked list in the order they appear.
    """

    nodes_list = []
    traverse(head, nodes_list)
    return nodes_list


def traverse(head, nodes):
    """
    Performs a depth-first traversal (recursive) of the linked list,
    appending the value of each node to the provided list.

    Args:
        head (Node): The current node in the traversal.
        nodes (list): The list to store the extracted node values.
    """

    if head is None:
        return  # Base case: Reached the end of the linked list

    nodes.append(head.val)
    traverse(head.next, nodes)  # Recursive call to traverse the next node

"""
Time Complexity: O(n)
The traverse function visits each node in the linked list exactly once.
In Big O notation, this represents a linear time complexity.

Space Complexity: O(n)
The node_values function creates a new list to store the extracted values.
In the worst case (where all nodes have unique values), the list will contain n elements,
resulting in a linear space complexity.

Notes on Approach and Reasoning:
This code utilizes a recursive approach to traverse the linked list.
At each node, the value is appended to the list, and then the function recursively calls itself
on the `next` node, effectively following the chain of nodes until the end is reached
(when head is None). This approach avoids the need for explicit loop management
for traversing the linked list.
"""
