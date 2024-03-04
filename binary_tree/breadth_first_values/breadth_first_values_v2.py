from collections import deque

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def breadth_first_values(root):
    """
    Performs breadth-first traversal of a binary tree and returns the values of the nodes in the traversal order.

    Args:
        root (Node): The root node of the binary tree.

    Returns:
        list: A list containing the values of the nodes in breadth-first traversal order.

    """
    if not root:  # If the tree is empty, return an empty list
        return []
    
    values = []  # List to store values of nodes in breadth-first traversal order
    queue = deque([root])  # Initialize deque with the root node

    while queue:  # Continue traversal until the deque is empty
        current = queue.popleft()  # Dequeue the leftmost node from the deque
        values.append(current)  # Append the value of the dequeued node to the values list

        if current.left:  # If the dequeued node has a left child, enqueue it
            queue.append(current.left)
        if current.right:  # If the dequeued node has a right child, enqueue it
            queue.append(current.right)
        
    return values  # Return the list of values in breadth-first traversal order

"""
Time Complexity Analysis:
- Enqueuing and dequeuing nodes: O(n), where n is the number of nodes in the binary tree.
Overall: O(n)

Space Complexity Analysis:
- Storing nodes in the deque: O(n), where n is the number of nodes in the binary tree.
- Storing values of nodes: O(n), where n is the number of nodes in the binary tree.
Overall: O(n)

Further Notes:
This algorithm performs a breadth-first traversal of a binary tree iteratively using a deque (double-ended queue). 
It starts from the root node and enqueues nodes at each level, and dequeues nodes in the order of their arrival, 
exploring nodes level by level. The values of the visited nodes are appended to a list in the order of traversal, 
and the final list of values is returned. The time complexity is O(n), and the space complexity is O(n).
"""


