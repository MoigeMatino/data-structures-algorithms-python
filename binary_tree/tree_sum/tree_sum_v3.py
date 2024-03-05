def tree_sum(root):
    """
    Calculates the sum of all node values in a binary tree iteratively using a stack.

    Args:
        root (Node): The root node of the binary tree.

    Returns:
        int: The sum of all node values in the binary tree.

    """
    stack = [root]  # Initialize stack with the root node
    sum = 0  # Initialize the sum of node values

    while stack:  # Continue traversal until the stack is empty
        current = stack.pop()  # Pop the top node from the stack
        sum += current.val  # Add the value of the popped node to the sum

        if current.right:  # If the popped node has a right child, push it onto the stack
            stack.append(current.right)

        if current.left:  # If the popped node has a left child, push it onto the stack
            stack.append(current.left)
    
    return sum  # Return the sum of all node values

"""
Time Complexity Analysis:
- Pushing and popping nodes onto/from stack: O(n), where n is the number of nodes in the binary tree.
Overall: O(n)

Space Complexity Analysis:
- Storing nodes in the stack: O(n), where n is the number of nodes in the binary tree.
Overall: O(n)

Further Notes:
This algorithm calculates the sum of all node values in a binary tree iteratively using a stack. 
It starts from the root node and pushes nodes onto the stack in a depth-first traversal manner. 
Nodes are popped from the stack, and their values are added to the sum. The right child is pushed 
before the left child to ensure that the left subtree is processed first. The time complexity is 
O(n), and the space complexity is O(n).
"""
