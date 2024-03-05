from collections import deque

def tree_min_value(root):
    """
    Finds the minimum value in a binary tree using breadth-first search iteratively.

    Args:
        root (Node): The root node of the binary tree.

    Returns:
        int: The minimum value in the binary tree.

    """
    min_val = float("inf")  # Initialize minimum value to positive infinity
    queue = deque([root])  # Initialize deque with the root node
    
    while queue:  # Continue traversal until the deque is empty
        current = queue.popleft()  # Dequeue the leftmost node from the deque
        
        if current.val < min_val:  # Update minimum value if current node value is smaller
            min_val = current.val
        
        if current.left:  # If the dequeued node has a left child, enqueue it
            queue.append(current.left)
        
        if current.right:  # If the dequeued node has a right child, enqueue it
            queue.append(current.right)
        
    return min_val  # Return the minimum value found in the binary tree

"""
Time Complexity Analysis:
- Enqueuing and dequeuing nodes: O(n), where n is the number of nodes in the binary tree.
Overall: O(n)

Space Complexity Analysis:
- Storing nodes in the deque: O(n), where n is the number of nodes in the binary tree.
Overall: O(n)

Further Notes:
This algorithm finds the minimum value in a binary tree using breadth-first search iteratively. 
It starts from the root node and enqueues nodes at each level, dequeuing nodes in the order 
of their arrival, exploring nodes level by level. The minimum value is updated whenever a 
smaller value is encountered during traversal. The time complexity is O(n), where n is the 
number of nodes in the binary tree, and the space complexity is O(n).
"""
