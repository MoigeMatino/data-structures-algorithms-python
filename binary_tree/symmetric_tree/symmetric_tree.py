from collections import deque

def symmetric_tree(root):
    """
    Determine if a binary tree is symmetric around its center.

    Parameters:
    root (Node): The root node of the binary tree.

    Returns:
    bool: True if the tree is symmetric, False otherwise.
    """
    queue = deque([root.left, root.right])
    
    while queue:
        curr_left = queue.popleft()
        curr_right = queue.popleft()
        
        # If both nodes are None, they are symmetric; continue to the next pair
        if not curr_left and not curr_right:
            continue
        
        # If only one of the nodes is None, the tree is not symmetric
        if not curr_right or not curr_left:
            return False
        
        # If the values of the nodes are not equal, the tree is not symmetric
        if curr_left.val != curr_right.val:
            return False
        
        # Append children in mirrored order to maintain symmetry check
        queue.append(curr_left.left)
        queue.append(curr_right.right)
        queue.append(curr_left.right)
        queue.append(curr_right.left)
        
    return True

# Approach:
#   ---------
#   The function uses an iterative approach with a queue to perform a level-order traversal,
#   comparing nodes in pairs to check for symmetry. The idea is to compare the left and right
#   subtrees of the tree simultaneously, ensuring that they mirror each other.

#   Steps:
#   1. Initialize a queue with the left and right children of the root.
#   2. While the queue is not empty, pop two nodes at a time (curr_left and curr_right).
#   3. If both nodes are None, continue to the next pair (they are symmetric).
#   4. If only one of the nodes is None, return False (they are not symmetric).
#   5. If the values of the nodes are not equal, return False (they are not symmetric).
#   6. Append the children of curr_left and curr_right to the queue in a mirrored order:
#      - Append curr_left.left and curr_right.right
#      - Append curr_left.right and curr_right.left
#   7. If all pairs are symmetric, return True.

#   Time Complexity:
#   ----------------
#   O(n), where n is the number of nodes in the tree. Each node is enqueued and dequeued once.

#   Space Complexity:
#   -----------------
#   O(n), where n is the number of nodes in the tree. In the worst case, the space used by the queue
#   is proportional to the number of nodes at the widest level of the tree, which can be up to n/2.