def tree_levels(root):
    """
    Collects the values of a binary tree's nodes level-by-level using Depth-First Search (DFS).

    Args:
        root: The root node of the binary tree.

    Returns:
        A list of lists, where each inner list represents the values of the nodes at a single level of the tree.
        If the tree is empty, returns an empty list.
    """

    levels = []  # Initialize an empty list to store node values per level
    _tree_levels(root, levels, 0)  # Start the recursive helper function
    return levels

def _tree_levels(root, levels, level_num):
    """
    Recursive helper function that traverses the tree using DFS and populates the `levels` list.

    Args:
        root: The current node being processed in the traversal.
        levels: The list to store node values for each level.
        level_num: The current level number during the traversal.
    """

    if root is None:  # Base case: Handle empty subtree
        return

    if level_num == len(levels):  # New level encountered, create a new list
        levels.append([root.val])
    else:  # Existing level, append node value to the corresponding list
        levels[level_num].append(root.val)

    _tree_levels(root.left, levels, level_num + 1)  # Recursively process left subtree
    _tree_levels(root.right, levels, level_num + 1)  # Recursively process right subtree

"""
**Time and Space Complexity:**

- Time Complexity: O(n), where n is the number of nodes in the tree. In the worst case, each node is visited exactly once.
- Space Complexity: O(n), due to the recursion stack. In the worst case (a skewed tree), the stack depth can be proportional 
to the tree's height, which can be n in the case of a complete binary tree.

**Approach and Reasoning:**

- This algorithm employs Depth-First Search (DFS) to traverse the tree recursively.
- It leverages a recursive helper function `_tree_levels` to explore each node and its descendants.
- The `levels` list is passed as a reference between function calls, allowing for dynamic updates during the traversal.
- The `level_num` variable keeps track of the current level during the recursion.
- When a new level is encountered (no corresponding list exists in `levels`), a new list is created and appended to `levels`.
- Otherwise, the node's value is appended to the existing list for its corresponding level.

**Notes:**

- This implementation assumes the existence of a `TreeNode` class representing a binary tree node with properties like `val`, `left`, and `right`.
- The space complexity of O(n) is due to the potential recursion depth, which can be high for skewed trees. For balanced trees, the space complexity would be closer to log(n).
"""
