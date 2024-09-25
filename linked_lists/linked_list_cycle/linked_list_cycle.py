def detect_cycle(head):
    """
    Detects if a cycle exists in a singly linked list.

    This function uses Floyd's Tortoise and Hare algorithm to determine if there is a cycle in the linked list.
    The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. If there is a cycle,
    the fast pointer will eventually meet the slow pointer. If the fast pointer reaches the end of the list, there is no cycle.

    Args:
        head: The head node of the singly linked list.

    Returns:
        True if a cycle is detected in the linked list, False otherwise.
    """
    if head is None:
        return None  # Return None if the list is empty, indicating no cycle
    
    slow = head  # Initialize the slow pointer to the head of the list
    fast = head  # Initialize the fast pointer to the head of the list
    
    # Traverse the list with the two pointers
    while fast and fast.next:
        slow = slow.next  # Move the slow pointer one step
        fast = fast.next.next  # Move the fast pointer two steps
        
        # If the slow and fast pointers meet, a cycle is detected
        if slow == fast:
            return True
    
    # If the fast pointer reaches the end of the list, there is no cycle
    return False

# Time Complexity: O(n)
# The algorithm runs in linear time because each pointer traverses the list at most once.
# The fast pointer moves through the list twice as fast as the slow pointer, ensuring that
# the entire list is traversed in O(n) time, where n is the number of nodes in the list.

# Space Complexity: O(1)
# The algorithm uses a constant amount of extra space. It only uses a few pointer variables
# (slow, fast) and does not require any additional data structures that depend on the size of the input list.

# Approach:
# The function employs Floyd's Tortoise and Hare algorithm, which is an efficient way to detect cycles in a linked list.
# By moving one pointer at half the speed of the other, if there is a cycle, the two pointers will eventually meet.
# This approach is optimal for cycle detection because it requires only a single pass through the list and uses constant space.