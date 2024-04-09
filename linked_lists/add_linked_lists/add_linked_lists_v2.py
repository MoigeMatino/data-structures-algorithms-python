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

def add_lists(head_1, head_2, carry=0):
    """
    Adds two linked lists representing non-negative integers (digits stored in reverse order).

    Args:
        head_1 (Node): The head node of the first linked list.
        head_2 (Node): The head node of the second linked list.
        carry (int, optional): Carryover value from the previous digit addition (default: 0).

    Returns:
        Node: The head node of the linked list representing the sum of the two input lists.
    """

    if head_1 is None and head_2 is None and carry == 0:
        # Base case: All lists are empty and there's no carry, so the sum is zero (None)
        return None

    val_1 = 0 if head_1 is None else head_1.val
    val_2 = 0 if head_2 is None else head_2.val

    # Calculate the sum of digits and potential carry
    sum = val_1 + val_2 + carry
    next_carry = 1 if sum > 9 else 0
    digit = sum % 10  # Extract the digit for the current node

    result = Node(digit)  # Create a new node for the current digit

    # Handle cases where one list might be shorter
    next_1 = None if head_1 is None else head_1.next
    next_2 = None if head_2 is None else head_2.next

    # Recursive call to add the remaining digits with the carry
    result.next = add_lists(next_1, next_2, next_carry)

    return result

# Time Complexity: O(max(n, m))
# The loop (implicit in recursion) continues as long as at least one of the lists or the carry is not zero.
# In the worst case, the longer list is iterated through completely.
# Therefore, the time complexity is proportional to the maximum length of the two lists (O(max(n, m))).

# Space Complexity: O(max(n, m))
# Due to recursion, the function call stack can grow up to the length of the longer list in the worst case.
# Each call in the stack stores references to local variables and return addresses, contributing to space complexity.

# Notes on Approach and Reasoning:
# This code implements a recursive approach to add two linked lists representing non-negative integers.
# It defines a base case for when all lists are empty and there's no carry (resulting in a sum of zero).
# In each recursive call:
#   - It handles cases where one list might be shorter by assigning 0 to the missing digit.
#   - It calculates the sum of the current digits from both lists and the carry.
#   - It updates the carry variable based on whether the sum exceeds 9.
#   - It extracts the digit for the current node by taking the modulo 10 of the sum.
#   - It creates a new node with the digit (`result`).
#   - It makes a recursive call to `add_lists` on the remaining parts of both lists (`next_1` and `next_2`), passing the carry (`next_carry`) for the next digit addition.
#   - The recursive call returns the linked list representing the sum of the remaining digits.
#   - The current node (`result`) sets its `next` pointer to the linked list returned by the recursive call, building the result list.
# Finally, the function returns the head node of the entire linked list representing the sum.

# This recursive approach is concise but might have higher space complexity due to the call stack compared to an iterative approach. 
