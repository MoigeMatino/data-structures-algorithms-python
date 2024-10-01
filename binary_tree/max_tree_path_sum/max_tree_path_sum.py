def max_tree_path_sum(root):
    """
    Calculate the maximum path sum in a binary tree. A path is defined as any sequence of nodes
    from some starting node to any node in the tree along the parent-child connections. The path
    does not need to go through the root, and it can start and end at any node.

    Parameters:
    root (Node): The root node of the binary tree.

    Returns:
    int: The maximum path sum found in the binary tree.
    """
    def max_contrib(node):
        if not node:
            return 0, float("-inf")
        
        # Recursively calculate the maximum contributions and path sums for left and right subtrees
        left_contrib, left_max = max_contrib(node.left)
        right_contrib, right_max = max_contrib(node.right)
        
        # Ensure only non-negative contributions are considered
        left_contrib = max(left_contrib, 0)
        right_contrib = max(right_contrib, 0)
        
        # Calculate the maximum path sum with the current node as the highest node
        current_max_sum = node.val + left_contrib + right_contrib
        
        # Determine the maximum path sum found so far
        max_sum = max(current_max_sum, left_max, right_max)
        
        # Calculate the maximum contribution to the parent node
        node_contrib = node.val + max(right_contrib, left_contrib)
        return node_contrib, max_sum
    
    # Start the recursion and return the maximum path sum found
    _, max_sum = max_contrib(root)
    
    return max_sum

# Approach and Reasoning:
#   -----------------------
#   The function uses a helper function `max_contrib` to recursively calculate two values for each node:
#   1. `node_contrib`: The maximum path sum that can be extended to the parent node. This is the node's
#      value plus the maximum contribution from either its left or right subtree, ensuring that only
#      non-negative contributions are considered.
#   2. `max_sum`: The maximum path sum found so far, which could be the maximum path sum through the
#      current node (including both left and right children) or the best path sum found in the left or
#      right subtrees.

#   The algorithm uses postorder traversal to ensure that each node's subtrees are fully processed before
#   calculating the path sum that includes the node itself; allows us to gather information from the bottom up. 
#   This is crucial for correctly determining the
#   maximum path sum that might pass through any node in the tree.

#   Time Complexity:
#   ----------------
#   The time complexity of this algorithm is O(n), where n is the number of nodes in the binary tree.
#   This is because each node is visited exactly once during the traversal.

#   Space Complexity:
#   -----------------
#   The space complexity is O(h), where h is the height of the tree. This is due to the recursive call
#   stack. In the worst case (a completely unbalanced tree), the height h can be n, leading to a space
#   complexity of O(n). In a balanced tree, the height is log(n), leading to a space complexity of O(log n).