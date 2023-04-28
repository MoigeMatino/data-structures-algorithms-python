def tree_value_count(root, target):
    if root is None:
        return 0

    stack = [root]
    count = 0
    while stack:
        current = stack.pop()

        if current.val == target:
            count += 1

        if current.right is not None:
            stack.append(current.right)
        
        if current.left is not None:
            stack.append(current.left)
        
    return count

"""
DFS iterative approach

n = number of nodes
Time: O(n)
Space: O(n)

"""