def paired_parentheses(string):
    opening = '('
    closing = ')'
    stack = []
    for char in string:
        if char == opening:
            stack.append(char)
        elif char == closing:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
        
    return True

