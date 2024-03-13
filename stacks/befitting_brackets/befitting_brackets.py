def befitting_brackets(string):
    braces_mappping = {
        '(':')',
        '{':'}',
        '[':']'
    }
    stack = []
    for char in string:
        if char in braces_mappping:
            stack.append(char)
        else:
            if not stack:
                return False
            opening_brace = stack.pop()
            if braces_mappping[opening_brace] != char:
                return False
    return len(stack) == 0