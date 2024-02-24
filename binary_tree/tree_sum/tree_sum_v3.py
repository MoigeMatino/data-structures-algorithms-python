def tree_sum(root):
    stack = [root]
    sum = 0
    while stack:
        current = stack.pop
        sum += current.val

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)
    
    return sum

    