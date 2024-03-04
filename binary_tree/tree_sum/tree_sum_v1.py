from collections import deque

def tree_sum(root):
    """
    Calculates the sum of all node values in a binary tree using breadth-first traversal.

    Args:
        root (Node): The root node of the binary tree.

    Returns:
        int: The sum of all node values in the binary tree.

    """
    if not root:  # If the tree is empty, return 0
        return 0
    
    sum = 0  # Initialize the sum of node values
    queue = deque([root])  # Initialize deque with the root node

    while queue:  # Continue traversal until the deque is empty
        current = queue.popleft()  # Dequeue the leftmost node from the deque
        sum += current.val  # Add the value of the dequeued node to the sum
        
        if current.left:  # If the dequeued node has a left child, enqueue it
            queue.append(current.left)
        
        if current.right:  # If the dequeued node has a right child, enqueue it
            queue.append(current.right)
        
    return sum  # Return the sum of all node values

"""
Time Complexity Analysis:
- Enqueuing and dequeuing nodes: O(n), where n is the number of nodes in the binary tree.
Overall: O(n)

Space Complexity Analysis:
- Storing nodes in the deque: O(n), where n is the number of nodes in the binary tree.
Overall: O(n)

Further Notes:
This algorithm calculates the sum of all node values in a binary tree using breadth-first traversal. 
It starts from the root node and enqueues nodes at each level, and dequeues nodes in the order of 
their arrival, exploring nodes level by level. The values of the visited nodes are added to the sum, 
and the final sum is returned. The time complexity is O(n), and the space complexity is O(n).
"""
