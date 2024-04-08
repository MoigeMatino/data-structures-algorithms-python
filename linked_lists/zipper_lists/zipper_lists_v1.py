def zipper_lists(head_1, head_2):
    """
    Zips together two linked lists iteratively.

    Args:
        head_1 (Node): The head node of the first linked list.
        head_2 (Node): The head node of the second linked list.

    Returns:
        Node: The head node of the zippered linked list.
    """

    tracker = head_1  # Initialize tracker to point to the first node
    current_1 = head_1.next  # Initialize pointer to the second node of list 1
    current_2 = head_2  # Initialize pointer to the head node of list 2
    count = 0  # Counter to determine which list to insert from

    while current_1 is not None and current_2 is not None:  # Loop until both lists are exhausted
        if count % 2 == 0:  # Even count: insert from list 2
            tracker.next = current_2
            current_2 = current_2.next
        else:  # Odd count: insert from list 1
            tracker.next = current_1
            current_1 = current_1.next

        tracker = tracker.next  # Move tracker to the inserted node
        count += 1  # Increment counter

    # Append remaining elements from the non-exhausted list
    tracker.next = current_1 if current_1 is not None else current_2

    return head_1

# Time Complexity: O(min(n, m))
# In the worst case, the loop iterates until the shorter list is exhausted.
# This results in a time complexity proportional to the minimum of the lengths (n, m) of the two lists.

# Space Complexity: O(1)
# The function uses constant extra space for pointers (`tracker`, `current_1`, `current_2`, and `count`),
# independent of the lengths of the input lists. This is considered constant space complexity.

# Notes on Approach and Reasoning:
# This code utilizes an iterative approach to create a zippered list from two input lists.
# It maintains pointers to the current nodes in both lists and a tracker to navigate the resulting list.
# A counter (`count`) determines which list to insert from in each iteration (even: list 2, odd: list 1).
# The loop continues until both lists are exhausted. After the loop, any remaining elements from the non-exhausted list 
# are appended to the end of the zippered list.
# This iterative approach is efficient for creating zippered lists and avoids the overhead associated with recursion.
