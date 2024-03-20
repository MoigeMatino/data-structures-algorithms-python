def nesting_score(string):
    stack = [0]
    for brace in string:
        if brace == '[':
            stack.append(0)
        else:
            popped_value = stack.pop()
            if popped_value == 0:
                stack[-1] += 1
            else:
                nested_score = popped_value * 2
                stack[-1] += nested_score
    return stack[0]

"""

    n = length of string
    Time: O(n)
    Space: O(n)

"""