from collections import deque
def bottom_right_value(root):
    if root is None:
        return None
    queue = deque([root])
    while queue:
        current = queue.popleft()
        
        if current.left is not None:
                queue.append(current.left)
        
        if current.right is not None:
            queue.append(current.right)
        
    return current.val

"""
BFS iterative approach
The reason we use BFS and not DFS is because DFS will get the right most value,
which may not necessarily be the BOTTOM right value. Consider this tree, DFS would return -13 
but the correct answer is 6. BFS will return the correct answer because of the way it traverses
the tree; level by level:
#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   -4   -13
#     / \       
#    -2  6

n = number of nodes
Time: O(n)
Space: O(n)

"""
