class Node:
    """
    Represents a node in a singly linked list.

    Attributes:
        val (int): The value stored in the node.
        next (Node): A reference to the next node in the linked list, or None if it's the last node.
    """

    def __init__(self, val):
        """
        Initializes a new Node instance.

        Args:
            val (int): The value to store in the node.
        """
        self.val = val
        self.next = None  # Initialize the next pointer to None by default

def traverse(head):
    """
    Traverses a singly linked list recursively and returns a list of all node values.

    Args:
        head (Node): The head node of the linked list, or None if the list is empty.

    Returns:
        list[int]: A list containing the values of all nodes in the linked list in the order they appear.

    Raises:
        TypeError: If the argument `head` is not a Node object.
    """

    if not isinstance(head, Node):  # Check if head is a valid Node object
        raise TypeError("head must be a Node object")

    if head is None:  # Base case: Empty list
        return []  # Return an empty list

    nodes = traverse(head.next)  # Recursive call to traverse the rest of the list
    nodes.append(head.val)  # Append the current node's value to the results

    return nodes

"""
Time Complexity: O(n)
The `traverse` function performs a recursive call for each node in the linked list, where n is the number of nodes. 
The total number of recursive calls is directly proportional to the number of nodes.

Space Complexity: O(n)
In the worst case (deeply nested linked list), the recursive calls create a call stack that grows with the depth 
of the list. The space complexity can be considered O(log n) for balanced linked lists.

Further Notes:
- **Recursive vs. Iterative Approach:** While recursive solutions can be elegant, iterative approaches might be preferable 
for very large linked lists due to the potential for stack overflow errors with deep recursion. An iterative approach could 
use a loop to traverse the list without building a call stack.

- **Error Handling:** The code now includes a check for the type of `head` and raises a `TypeError` if it's not a `Node` object. 
Consider adding checks for other potential errors, such as circular references in the linked list.
"""
