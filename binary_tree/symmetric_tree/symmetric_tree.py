from collections import deque
def symmetric_tree(root):
    queue = deque([root.left, root.right])
    
    while queue:
        curr_left = queue.popleft()
        curr_right = queue.popleft()
        
        if not curr_left and not curr_right:
            continue
        
        if not curr_right or not curr_left:
            return False
        
        if curr_left.val != curr_right.val:
            return False
        
        queue.append(curr_left.left)
        queue.append(curr_right.right)
        queue.append(curr_left.right)
        queue.append(curr_right.left)
        
    return True