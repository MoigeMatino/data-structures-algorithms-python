def invert_tree(root):
    """
    Invert a binary tree by swapping the left and right children of all nodes.

    Parameters:
    root (Node): The root node of the binary tree.

    Returns:
    Node: The root node of the inverted binary tree.
    """
    if root is None:
        return None

    # Recursively invert the left subtree
    if root.left:
        invert_tree(root.left)

    # Recursively invert the right subtree
    if root.right:
        invert_tree(root.right)

    # Swap the left and right children
    root.left, root.right = root.right, root.left

    return root


## Approach and Reasoning

### Postorder Traversal

# The `invert_tree` function uses a postorder traversal approach, which is particularly well-suited for this task. Here's why:

# 1. **Subtree Completion Before Swapping**:
#    - Postorder traversal processes the left and right subtrees before the node itself. This ensures that both subtrees are 
# fully inverted before swapping the children of the current node. This is crucial for maintaining the correct structure of the inverted tree.

# 2. **Recursive Nature**:
#    - The recursive nature of postorder traversal aligns perfectly with the requirement to process subtrees before the node. 
# This allows the function to handle each subtree independently and ensures that the inversion is applied correctly at every level of the tree.

# 3. **Simplicity and Clarity**:
#    - Using postorder traversal makes the code straightforward and easy to understand. It naturally fits the recursive structure 
# of the function, where you first handle the base case (null nodes), then recursively process subtrees, and finally perform the swap operation.

### Why Not Preorder or Inorder?

# - **Preorder Traversal** (node, left, right) would attempt to swap the children before the subtrees are inverted, leading to incorrect results.
# - **Inorder Traversal** (left, node, right) does not naturally fit the requirement of processing both subtrees before the node itself, 
# making it less suitable for this task.

## Complexity Analysis

# - **Time Complexity**:
#   - The time complexity of the `invert_tree` function is O(n), where n is the number of nodes in the tree. This is because each node is visited 
# exactly once to swap its children.

# - **Space Complexity**:
#   - The space complexity is O(h), where h is the height of the tree. This is due to the recursive call stack. In the worst case (a completely 
# unbalanced tree), the height $h$ can be $n$, leading to a space complexity of $O(n)$. In a balanced tree, the height is $\log n$, leading to a 
# space complexity of O(log n).