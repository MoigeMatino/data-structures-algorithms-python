from collections import deque

def tree_includes(root, target):
    """
    Checks if a binary tree contains a specific value using breadth-first search.

    Args:
        root (Node): The root node of the binary tree.
        target: The value to search for in the binary tree.

    Returns:
        bool: True if the target value is found in the binary tree, False otherwise.

    """
    if root is None:  # If the root is None, return False
        return False
    
    queue = deque([root])  # Initialize deque with the root node

    while queue:  # Continue traversal until the deque is empty
        current = queue.popleft()  # Dequeue the leftmost node from the deque
        
        if current.val == target:  # If the value of the dequeued node matches the target value, return True
            return True
        
        if current.left:  # If the dequeued node has a left child, enqueue it
            queue.append(current.left)
        
        if current.right:  # If the dequeued node has a right child, enqueue it
            queue.append(current.right)
        
    return False  # If the target value is not found in the binary tree, return False

"""
Time Complexity Analysis:
- Enqueuing and dequeuing nodes: O(n), where n is the number of nodes in the binary tree.
Overall: O(n)

Space Complexity Analysis:
- Storing nodes in the deque: O(n), where n is the number of nodes in the binary tree.
Overall: O(n)

Further Notes:
This algorithm checks if a binary tree contains a specific value using breadth-first search. 
It starts from the root node and enqueues nodes at each level, and dequeues nodes in the 
order of their arrival, exploring nodes level by level. If the target value is found in 
the binary tree, the function returns True; otherwise, it returns False. The time complexity 
is O(n), and the space complexity is O(n).
"""
