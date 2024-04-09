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

def insert_node(head, value, index, count=0):
    """
    Inserts a new node with the specified value at a given index in the linked list (recursive approach).

    Args:
        head (Node): The head node of the linked list.
        value (int): The value to be inserted into the list.
        index (int): The index at which to insert the new node (0-based indexing).
        count (int, optional): Internal counter variable for recursion (default: 0).

    Returns:
        Node: The head node of the modified linked list with the new node inserted.
    """

    if index == 0:  # Base case: Inserting at the beginning
        new_head = Node(value)
        new_head.next = head
        return new_head

    if count == index - 1:  # Base case: Reached the insertion position
        temp = head.next
        head.next = Node(value)
        head.next.next = temp
        return

    # Recursive call to insert at the next node (for non-base cases)
    head.next = insert_node(head.next, value, index, count + 1)

    return head

# Time Complexity: O(n)
# In the worst case (inserting at the end), the function makes recursive calls until it reaches the end of the list.
# This results in linear time complexity proportional to the list's length.

# Space Complexity: O(n)
# Due to recursion, the function call stack can grow up to the list's length in the worst case,
# leading to linear space complexity.

# Notes on Approach and Reasoning:
# This code implements a recursive approach to insert a new node with a given value at a specified index in the linked list.
# It defines a base case for inserting at the beginning (index 0).
# Another base case checks if the current node's position (`count`) matches the desired insertion index (index-1).
# If the position is found, it stores the next node (`temp`) for later linking and creates/links the new node.
# For non-base cases, it makes a recursive call to `insert_node` on the `head.next` node, incrementing the internal counter (`count`).
# This continues until the desired insertion position is reached in the recursion.
# After the recursive call returns (with the modified list), it updates the current node's `next` pointer (important for maintaining the overall linked list structure).
# Finally, it returns the (potentially modified) head node.

# This recursive approach is concise but might have higher space complexity due to the call stack compared to the iterative approach.
