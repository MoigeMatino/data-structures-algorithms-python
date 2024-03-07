def tree_value_count(root, target):
    """
    Count the occurrences of a target value in the binary tree using iterative depth-first traversal.

    Args:
    - root: The root node of the binary tree.
    - target: The value to count occurrences of.

    Returns:
    - int: The number of occurrences of the target value in the binary tree.

    """

    # Base case: If the root is None, return 0
    if root is None:
        return 0

    # Initialize a stack for iterative depth-first traversal
    stack = [root]
    count = 0

    # Iterate through the binary tree using iterative depth-first traversal
    while stack:
        current = stack.pop()

        # If the value of the current node matches the target value, increment count
        if current.val == target:
            count += 1

        # Add the right child to the stack if it exists
        if current.right is not None:
            stack.append(current.right)
        
        # Add the left child to the stack if it exists
        if current.left is not None:
            stack.append(current.left)
        
    return count

"""
Time Complexity Analysis:
- Each node is visited once: O(n), where n is the number of nodes in the binary tree.

Space Complexity Analysis:
- Stack space for iterative traversal: O(h), where h is the height of the binary tree (worst-case scenario).
Overall: O(h)

Further Notes:
Iterative depth-first traversal is used to traverse the binary tree.
At each node, the algorithm checks if the value of the node matches the target value.
If it matches, it increments the count by 1.
The algorithm iterates through the tree while maintaining a stack of nodes to visit next.
This approach avoids using recursion and instead uses a stack to keep track of nodes to visit.
"""
