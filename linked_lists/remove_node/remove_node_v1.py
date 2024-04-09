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

def remove_node(head, target_val):
    """
    Removes the first node from the linked list that has the specified target value.

    Args:
        head (Node): The head node of the linked list.
        target_val (int): The value to be removed from the list.

    Returns:
        Node: The head node of the modified linked list, potentially with the target node removed.
    """

    prev = None  # Initialize variable to store the previous node
    current = head  # Initialize current node pointer to the head

    # Special case: Head node is the target node
    if head.val == target_val:
        return head.next  # Return the next node as the new head

    while current is not None:  # Iterate through the linked list
        if current.val == target_val:  # Check if current node's value matches the target
            if prev is not None:  # If not the head node, update the previous node's next pointer
                prev.next = current.next
            break  # Exit the loop after removing the target node

        prev = current  # Update prev to point to the current node for next iteration
        current = current.next  # Move current pointer to the next node

    return head  # Return the (potentially modified) head node

# Time Complexity: O(n)
# The while loop iterates through the linked list in the worst case (target value exists at the end).
# This results in linear time complexity proportional to the list's length.

# Space Complexity: O(1)
# The function uses constant extra space for variables (prev, current), independent of the linked list's size.
# This is considered constant space complexity.

# Notes on Approach and Reasoning:
# This code implements an iterative approach to remove the first occurrence of a target value from a linked list.
# It initializes variables to track the previous node and the current node.
# It first checks if the head node itself is the target node and returns the next node as the new head if so.
# Then, it iterates through the linked list. In each iteration:
#   - It checks if the current node's value matches the target value.
#   - If it's a match, it checks if it's the head node (using the prev variable).
#     - If not the head node, it updates the previous node's next pointer to skip the target node.
#   - It updates the prev and current pointers for the next iteration.
# After iterating through the list, the function returns the (potentially modified) head node.
# This approach avoids recursion and modification of the original head pointer within the function.
