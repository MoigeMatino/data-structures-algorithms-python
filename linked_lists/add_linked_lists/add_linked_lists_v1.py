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
            val (int): The value stored in the node.
        """
        self.val = val
        self.next = None

def add_lists(head_1, head_2):
    """
    Adds two linked lists representing non-negative integers (digits stored in reverse order).

    Args:
        head_1 (Node): The head node of the first linked list.
        head_2 (Node): The head node of the second linked list.

    Returns:
        Node: The head node of the linked list representing the sum of the two input lists.
    """

    dummy_head = Node(None)  # Create a dummy head for the resulting list
    tail = dummy_head  # Initialize tail pointer to the dummy head

    carry = 0  # Variable to store carryover from digit addition

    current_1 = head_1  # Pointer to the first list's head node
    current_2 = head_2  # Pointer to the second list's head node

    while current_1 is not None or current_2 is not None or carry == 1:
        # Handle cases where one list might be shorter than the other
        val_1 = 0 if current_1 is None else current_1.val
        val_2 = 0 if current_2 is None else current_2.val

        # Calculate the sum of digits and potential carry
        sum = val_1 + val_2 + carry
        carry = 1 if sum > 9 else 0
        digit = sum % 10  # Extract the digit for the current node

        # Create a new node for the digit and append it to the result list
        tail.next = Node(digit)
        tail = tail.next

        # Move pointers to the next nodes in each list (if applicable)
        if current_1 is not None:
            current_1 = current_1.next
        if current_2 is not None:
            current_2 = current_2.next

    return dummy_head.next  # Return the actual head node (excluding the dummy head)

# Time Complexity: O(max(n, m))
# The loop continues as long as at least one of the lists or the carry is not zero.
# In the worst case, the longer list is iterated through completely.
# Therefore, the time complexity is proportional to the maximum length of the two lists (O(max(n, m))).

# Space Complexity: O(max(n, m))
# In the worst case, the function creates a new node for each digit in the longer list.
# This results in space complexity proportional to the maximum length of the two lists (O(max(n, m))).

# Notes on Approach and Reasoning:
# This code implements a function to add two linked lists representing non-negative integers.
# It uses a dummy head node to simplify handling the creation of the resulting list.
# A carry variable is used to track any carryover from digit addition.
# The code iterates while at least one of the lists or the carry is not zero.
# In each iteration:
#   - It handles cases where one list might be shorter by assigning 0 to the missing digit.
#   - It calculates the sum of the current digits from both lists and the carry.
#   - It updates the carry variable based on whether the sum exceeds 9.
#   - It extracts the digit for the current node by taking the modulo 10 of the sum.
#   - It creates a new node with the digit and appends it to the result list using the tail pointer.
#   - It moves the pointers to the next nodes in each list (if they exist).
# Finally, the function returns the actual head node of the resulting linked list (excluding the dummy head).

# This approach efficiently handles lists of different lengths and correctly calculates the sum with carryover.
