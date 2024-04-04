def get_node_value(head, index):
    """
    Retrieves the value of a node at a specific index in a linked list.

    Args:
        head (Node): The head node of the linked list.
        index (int): The index of the node to retrieve the value from.

    Returns:
        int: The value stored in the node at the specified index, or None if the index is invalid.
    """

    if index < 0:  # Handle negative indexes (invalid)
        return None

    counter = 0
    current = head

    while current is not None:  # Iterate through the linked list
        if counter == index:  # Check if current node's index matches the target index
            return current.val  # Found the target node, return its value

        current = current.next  # Move to the next node
        counter += 1  # Increment counter for the next iteration

    return None  # Reached the end without finding the target index, return None

# Time Complexity: O(n)
# In the worst case, the `while` loop iterates through the entire linked list
# (n nodes) if the target node is at the end or the index is out of bounds.
# This results in a linear time complexity proportional to the number of nodes (n).

# Space Complexity: O(1)
# The function uses constant extra space for the `counter` and `current` variables,
# independent of the linked list's size. This is considered constant space complexity.

# Notes on Approach and Reasoning:
# This code utilizes an iterative approach to access the value at a specific index within the linked list.
# It first checks for an invalid negative index and returns None in that case.
# Then, it iterates through the list using a `while` loop and a counter variable.
# Inside the loop, the current node's index (counter) is compared to the target index.
# If a match is found, the function immediately returns the current node's value.
# If the loop completes without finding a matching index, it returns None, indicating an invalid index.
# This iterative approach is generally efficient for accessing elements by index. 
