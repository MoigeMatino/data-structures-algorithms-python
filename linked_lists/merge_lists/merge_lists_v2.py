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
    Merges two sorted linked lists recursively.

    Args:
        head_1 (Node): The head node of the first sorted linked list.
        head_2 (Node): The head node of the second sorted linked list.

    Returns:
        Node: The head node of the merged and sorted linked list, or None if both lists are empty.
    """

    if head_1 is None and head_2 is None:  # Base case: Both lists are empty
        return None

    # Handle empty individual lists (prepend the non-empty list)
    if head_1 is None:
        return head_2
    elif head_2 is None:
        return head_1

    # Choose the smaller head node as the starting point for the merged list
    if head_1.val < head_2.val:
        next_1 = head_1.next  # Store the next node of list 1
        head_1.next = merge_lists(next_1, head_2)  # Recursive call with remaining elements
        return head_1
    else:
        next_2 = head_2.next  # Store the next node of list 2
        head_2.next = merge_lists(head_1, next_2)  # Recursive call with remaining elements
        return head_2

# Time Complexity: O(min(n, m))
# In the worst case, the recursive function calls itself until the shorter list is exhausted.
# This results in a time complexity proportional to the minimum of the lengths (n, m) of the two sorted lists.

# Space Complexity: O(min(n, m))
# Due to recursion, each function call creates a stack frame on the call stack.
# The depth of the call stack grows with the number of recursive calls, which is proportional 
# to the length of the shorter list (min(n, m)) in the worst case.
# This leads to a space complexity of O(min(n, m)).

# Notes on Approach and Reasoning:
# This code implements a recursive approach to merge two sorted linked lists.
# It checks for base cases: both lists empty or individual lists being empty.
# In each recursive call, it chooses the smaller head node as the starting point for the merged list.
# It stores the next node of the chosen list and makes a recursive call with the remaining elements of 
# both lists (the chosen list's next node and the other entire list).
# The recursive calls build the merged list by prepending the smaller nodes at each level.
# While concise, recursion can be less space-efficient for very long lists due to the call stack usage.
# For extremely large lists, an iterative approach might be preferable due to its constant space complexity.
