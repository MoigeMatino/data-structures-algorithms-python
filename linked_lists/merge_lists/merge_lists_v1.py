class Node:
    """
    Represents a node in a linked list.
    """
    def __init__(self, val):
        """
        Initializes a new Node object.

        Args:
            val (int): The value stored in the node.
        """
        self.val = val
        self.next = None  # Reference to the next node in the linked list (initially None)

def merge_lists(head_1, head_2):
    """
    Merges two sorted linked lists iteratively.

    Args:
        head_1 (Node): The head node of the first sorted linked list.
        head_2 (Node): The head node of the second sorted linked list.

    Returns:
        Node: The head node of the merged and sorted linked list.
    """

    dummy_head = Node(None)  # Create a dummy head node for the merged list
    tracker = dummy_head  # Tracker to traverse the merged list

    while head_1 is not None and head_2 is not None:  # Loop until both lists are exhausted
        if head_1.val < head_2.val:  # Choose the smaller value
            tracker.next = head_1
            head_1 = head_1.next
        else:
            tracker.next = head_2
            head_2 = head_2.next

        tracker = tracker.next  # Move tracker to the appended node

    # Append remaining elements from the non-exhausted list
    tracker.next = head_1 if head_1 is not None else head_2

    return dummy_head.next  # Return the head of the merged list (excluding the dummy head)

# Time Complexity: O(min(n, m))
# In the worst case, the loop iterates until the shorter list is exhausted.
# This results in a time complexity proportional to the minimum of the lengths (n, m) of the two sorted lists.

# Space Complexity: O(1)
# The function uses constant extra space for pointers (`dummy_head`, `tracker`, `head_1`, and `head_2`),
# independent of the lengths of the input lists. This is considered constant space complexity.

# Notes on Approach and Reasoning:
# This code utilizes an iterative approach to merge two sorted linked lists.
# It creates a dummy head node for the merged list and a tracker to navigate it.
# The loop compares the values of the current nodes in both lists and chooses the smaller value.
# The chosen node is then appended to the merged list using the tracker.
# The loop continues until both input lists are exhausted. After the loop, any remaining elements from the 
# non-exhausted list are appended to the end of the merged list.
# This iterative approach is efficient for merging sorted linked lists and avoids the overhead associated with recursion.
