def get_middle_node(head):
    """
    Finds the middle node of a singly linked list.

    This function uses the two-pointer technique, often referred to as the "Tortoise and Hare" approach,
    to efficiently find the middle node of a linked list. The slow pointer moves one step at a time,
    while the fast pointer moves two steps at a time. When the fast pointer reaches the end of the list,
    the slow pointer will be at the middle node.

    Args:
        head: The head node of the singly linked list.

    Returns:
        The middle node of the linked list. If the list is empty, returns None.
    """
    slow = head  # Initialize the slow pointer to the head of the list
    fast = head  # Initialize the fast pointer to the head of the list
    
    # Traverse the list with the two pointers
    while fast and fast.next:
        slow = slow.next  # Move the slow pointer one step
        fast = fast.next.next  # Move the fast pointer two steps
    
    # When the loop ends, the slow pointer is at the middle node
    return slow

# Time Complexity: O(n)
# The algorithm runs in linear time because each pointer traverses the list at most once.
# The fast pointer moves through the list twice as fast as the slow pointer, ensuring that
# the entire list is traversed in O(n) time, where n is the number of nodes in the list.

# Space Complexity: O(1)
# The algorithm uses a constant amount of extra space. It only uses a few pointer variables
# (slow, fast) and does not require any additional data structures that depend on the size of the input list.

# Approach:
# The function employs the "Tortoise and Hare" technique, which is an efficient way to find the middle
# of a linked list. By moving one pointer at half the speed of the other, the slower pointer will
# reach the middle of the list by the time the faster pointer reaches the end. This approach is
# optimal for finding the middle node in a single pass without needing to know the length of the list
# beforehand.