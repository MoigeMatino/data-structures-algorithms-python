class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def max_path_sum(root):
    if root is None:
        return float("-inf")
    
    if root.left is None and root.right is None:
        return root.val
    
    max_left = max_path_sum(root.left)
    max_right = max_path_sum(root.right)
    return root.val + max(max_left, max_right)

"""
n - number of nodes
Time: O(n)
Space: O(n)

TODO:
An iteration of this problem is the Binary Tree Maximum Path Sum
This problem tries to find the max path sum that mmay or may not include 
the root. More on this...
"""
