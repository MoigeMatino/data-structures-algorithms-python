def tree_min_value(root):
    stack = [root]
    min = float("inf")
    while stack:
        current = stack.pop()
        if current.val < min:
            min = current.val
        
        if current.left:
            stack.append(current.left)

        if current.right:
            stack.append(current.right)

        
    return min    

"""
DFS iterative approach

n = number of nodes
Time: O(n)
Space: O(n)

"""