def reverse_stack(stack):
    def insert_at_bottom(stack, item):
        if not stack:
            stack.append(item)
            return
        temp = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(temp)

    if not stack:
        return []
    item = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, item)
    return stack



        
