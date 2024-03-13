def paired_parentheses(string):
    count_of_open_parentheses = 0
    for char in string:
        if char == '(':
            count_of_open_parentheses += 1
        elif char == ')':
            if count_of_open_parentheses == 0:
                return False
            count_of_open_parentheses -= 1
        
    return count_of_open_parentheses == 0