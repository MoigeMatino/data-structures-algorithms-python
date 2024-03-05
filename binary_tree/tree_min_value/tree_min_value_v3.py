def tree_min_value(root):
    """
    Finds the minimum value in a binary tree using depth-first search iteratively.

    Args:
        root (Node): The root node of the binary tree.

    Returns:
        int: The minimum value in the binary tree.

    """
    stack = [root]  # Initialize stack with the root node
    min_val = float("inf")  # Initialize min_val to positive infinity
    
    while stack:  # Continue traversal until the stack is empty
        current = stack.pop()  # Pop the top node from the stack
        
        if current.val < min_val:  # Update min_val if current node value is smaller
            min_val = current.val
        
        if current.left:  # If the popped node has a left child, push it onto the stack
            stack.append(current.left)

        if current.right:  # If the popped node has a right child, push it onto the stack
            stack.append(current.right)
        
    return min_val  # Return the minimum value found in the binary tree

"""
Time Complexity Analysis:
- Pushing and popping nodes from the stack: O(n), where n is the number of nodes in the binary tree.
Overall: O(n)

Space Complexity Analysis:
- Storing nodes in the stack: O(n), where n is the number of nodes in the binary tree.
Overall: O(n)

Further Notes:
This algorithm finds the minimum value in a binary tree using depth-first search iteratively. 
It starts from the root node and iteratively explores nodes in a depth-first manner, updating 
the minimum value whenever a smaller value is encountered during traversal. The time complexity 
is O(n), where n is the number of nodes in the binary tree, and the space complexity is O(h), 
where h is the height of the binary tree in the worst-case scenario.
"""
