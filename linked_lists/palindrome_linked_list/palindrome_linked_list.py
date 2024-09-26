def palindrome(head):
    """
    Determines if a singly linked list is a palindrome.

    This function checks if the linked list is a palindrome by using a two-pointer technique to find the middle of the list,
    reversing the second half of the list, and then comparing the two halves.

    Args:
        head: The head node of the singly linked list.

    Returns:
        True if the linked list is a palindrome, False otherwise.
    """
    if head is None:
        return True  # An empty list is considered a palindrome
    
    slow = head  # Initialize the slow pointer to the head of the list
    fast = head  # Initialize the fast pointer to the head of the list
    
    # Find the middle of the linked list
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse the second half of the list
    reversed_half_head = reverse_list(slow)
    
    # Compare the first half and the reversed second half
    is_identical = compare_halfs(head, reversed_half_head)
    
    # retain linked list in the original order
    reverse_list(reversed_half_head)
    
    # Return the result of the comparison
    return is_identical

def reverse_list(head):
    """
    Reverses a singly linked list.

    Args:
        head: The head node of the list to be reversed.

    Returns:
        The new head of the reversed list.
    """
    prev = None
    current = head
    
    while current:
        next_node = current.next  # Store the next node
        current.next = prev  # Reverse the current node's pointer
        prev = current  # Move prev to the current node
        current = next_node  # Move to the next node
    
    return prev

def compare_halfs(head1, head2):
    """
    Compares two halves of a linked list to check for equality.

    Args:
        head1: The head of the first half of the list.
        head2: The head of the second half of the list.

    Returns:
        True if the two halves are identical, False otherwise.
    """
    while head1 and head2:
        if head1.val != head2.val:
            return False  # Return False if any values differ
        head1 = head1.next
        head2 = head2.next
    return True  # Return True if all values are identical

# Time Complexity: O(n)
# The algorithm runs in linear time because it involves three main steps: finding the middle of the list,
# reversing the second half, and comparing the two halves. Each of these steps requires a single pass through the list.

# Space Complexity: O(1)
# The algorithm uses a constant amount of extra space. It only uses a few pointer variables and does not require
# any additional data structures that depend on the size of the input list.

# Approach:
# 1. Use the two-pointer technique to find the middle of the linked list.
# 2. Reverse the second half of the list.
# 3. Compare the first half and the reversed second half to check for palindrome properties.
# This approach efficiently determines if the list is a palindrome without using extra space for storing values.