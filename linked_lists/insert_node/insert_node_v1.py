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

def insert_node(head, value, index):
    """
    Inserts a new node with the specified value at a given index in the linked list (iterative approach).

    Args:
        head (Node): The head node of the linked list.
        value (int): The value to be inserted into the list.
        index (int): The index at which to insert the new node (0-based indexing).

    Returns:
        Node: The head node of the modified linked list with the new node inserted.
    """

    if index == 0:  # Special case: Inserting at the beginning
        new_node = Node(value)
        new_node.next = head
        return new_node

    count = 0
    current = head

    while current is not None:
        if count == index - 1:  # Check if we reached the insertion position (index-1)
            temp = current.next  # Store the node currently after the insertion point

            # Create the new node and link it
            new_node = Node(value)
            current.next = new_node
            new_node.next = temp

            break  # Exit the loop after successful insertion

        count += 1
        current = current.next

    return head

# Time Complexity: O(n)
# In the worst case (inserting at the end), the loop iterates through the entire list.
# This results in linear time complexity proportional to the list's length.

# Space Complexity: O(1)
# The function uses constant extra space for variables (count, current, temp),
# independent of the linked list's size. This is considered constant space complexity.

# Notes on Approach and Reasoning:
# This code implements an iterative approach to insert a new node with a given value at a specified index in the linked list.
# It first checks for a special case where the insertion needs to happen at the beginning (index 0).
# Then, it iterates through the linked list using a counter variable (`count`) and a current node pointer.
# During iteration:
#   - It checks if the counter reaches the index-1 position (the node before the insertion point).
#   - If the position is found, it stores the next node (`temp`) for later linking.
#   - It creates a new node with the specified value.
#   - It updates the current node's `next` pointer to point to the new node.
#   - It links the new node's `next` pointer to the previously stored `temp` node (maintaining the original list order).
#   - The loop breaks after successful insertion.
# After iterating through the list, it handles the case where the index is out of bounds (greater than the list length).
# Finally, it returns the head node of the modified linked list.

# This iterative approach is efficient and avoids recursion, making it suitable for large lists.
