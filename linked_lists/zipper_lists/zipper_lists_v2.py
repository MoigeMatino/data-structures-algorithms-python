def zipper_lists(head_1, head_2):
    """
    Zips together two linked lists recursively.

    Args:
        head_1 (Node): The head node of the first linked list.
        head_2 (Node): The head node of the second linked list.

    Returns:
        Node: The head node of the zippered linked list, or None if both lists are empty.
    """

    if head_1 is None and head_2 is None:  # Base case: Both lists are empty
        return None

    # Handle empty individual lists (prepend the non-empty list)
    if head_1 is None:
        return head_2
    elif head_2 is None:
        return head_1

    next_1 = head_1.next  # Store the next node of list 1
    next_2 = head_2.next  # Store the next node of list 2

    # Link current nodes: head_1 points to head_2
    head_1.next = head_2

    # Recursive call to zipper the remaining lists (next_1 and next_2)
    head_2.next = zipper_lists(next_1, next_2)  # head_2 points to the zippered result

    return head_1  # Return the head of the original list 1 (now zippered)

# Time Complexity: O(min(n, m))
# In the worst case, the recursive function calls itself until the shorter list is exhausted.
# This results in a time complexity proportional to the minimum of the lengths (n, m) of the two lists.

# Space Complexity: O(min(n, m))
# Due to recursion, each function call creates a stack frame on the call stack.
# The depth of the call stack grows with the number of recursive calls, which is proportional 
# to the length of the shorter list (min(n, m)) in the worst case.
# This leads to a space complexity of O(min(n, m)).

# Notes on Approach and Reasoning:
# This code implements a recursive approach to create a zippered list from two input lists.
# It checks for base cases: both lists empty or individual lists being empty.
# In each recursive call, it stores the next nodes of both lists.
# Then, it links the current nodes (head_1 points to head_2).
# Finally, it makes a recursive call with the remaining portions of the lists (next_1 and next_2).
# The recursive calls build the zippered list by linking nodes alternately.
# While concise, recursion can be less space-efficient for very long lists due to the call stack usage.
# For extremely large lists, an iterative approach might be preferable due to its constant space complexity.
