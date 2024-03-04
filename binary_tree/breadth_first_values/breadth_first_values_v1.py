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
    queue = [root]  # Initialize queue with the root node

    while queue:  # Continue traversal until the queue is empty
        current = queue.pop(0)  # Dequeue the front node from the queue
        values.append(current)  # Append the value of the dequeued node to the values list

        if current.left:  # If the dequeued node has a left child, enqueue it
            queue.append(current.left)
        if current.right:  # If the dequeued node has a right child, enqueue it
            queue.append(current.right)
        
    return values  # Return the list of values in breadth-first traversal order

"""
Time Complexity Analysis:
- Popping elements from the queue and traversing each node once: O(n^2), where n is the number of nodes in the binary tree.
Overall: O(n^2)

Space Complexity Analysis:
- Storing nodes in the queue: O(n), where n is the number of nodes in the binary tree.
- Storing values of nodes: O(n), where n is the number of nodes in the binary tree.
Overall: O(n)

Further Notes:
This algorithm performs a breadth-first traversal of a binary tree iteratively using a queue. 
It starts from the root node and enqueues nodes at each level, and dequeues nodes in the order 
of their arrival, exploring nodes level by level. The values of the visited nodes are appended 
to a list in the order of traversal, and the final list of values is returned. The time complexity 
is O(n^2), and the space complexity is O(n).
The time complexity is O(n^2) because in each iteration of the while loop, queue.pop(0) is used to dequeue 
the front element from the queue. In Python lists, the pop(0) operation takes O(n) time complexity 
because it needs to shift all the remaining elements in the list to fill the gap left by the removed 
element. This shifting operation becomes increasingly expensive as the size of the list grows. Since the 
pop(0) operation is performed for each node in the binary tree, and each node is visited exactly once in the 
traversal, the total time complexity becomes O(n^2), where n is the number of nodes in the binary tree.
"""

