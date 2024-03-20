def nesting_score(string):
    """
    Calculates the nesting score of a string containing square brackets '[]'.

    Args:
        string: The string to be evaluated for nesting score. The string can only
                contain square brackets '[]'.

    Returns:
        The total nesting score of the brackets in the string.

    """

    stack = [0]  # Stack to keep track of current nesting depth and accumulated score

    for brace in string:
        if brace == '[':  # Encountering an opening bracket '['
            """
            # Push a new level onto the stack
            When encountering an opening bracket, push a new level (0) onto the stack.
            This represents a new nesting level starting at a score of 0.
            """
            stack.append(0)
        else:  # Encountering a closing bracket ']'
            """
            # Handle closing bracket ']'
            If the character is a closing bracket, pop the value from the stack. This
            value represents the score accumulated at the current nesting level.
            
            - Check for closing bracket:
                If the popped value is 0, it signifies an unmatched opening bracket which is now getting closed 
                with this closing bracket encounter. Add 1 to the new top value in the stack.

            - Update score for the previous level:
                If the popped value is not 0 (score accumulated from other previous nested levels ), calculate
                the score for the nested level. The score for the nested level is
                double the score of the current level that just closed.
                Add this score to the top element (previous level) remaining on the stack.
            """
            popped_value = stack.pop()
            if popped_value == 0:
                stack[-1] += 1
            else:
                nested_score = popped_value * 2  # Calculate score for previous level(s)
                stack[-1] += nested_score  # Update score on the previous level

    return stack[0]  # Return the score from the remaining element (top level)

"""
Complexity Analysis

    - n is the length of the input string.

Time Complexity: O(n)
The algorithm iterates through the string once (O(n)) and performs constant time operations (O(1)) like stack push/pop,
comparisons, and arithmetic operations. The number of stack operations is proportional to the number of brackets, which 
is typically less than or equal to the string length.

Space Complexity: O(n)
The stack can grow up to a depth equal to the number of opening brackets '[' in the string. In the worst case, all brackets 
might be opening brackets, leading to a stack size of n. However, for strings with properly nested brackets, the stack size
will be balanced and typically much smaller than n.

Further Notes:

* The algorithm efficiently calculates the nesting score using a stack to track nesting depth.

Approach Reasoning:

This algorithm leverages a stack to maintain information about the current nesting level and the accumulated score at each level. 
As we iterate through the string:

1. For an opening bracket '[':
   - We push a new level (0) onto the stack, signifying the start of a new nesting level with a score of 0.
2. For a closing bracket ']':
   - We pop the top element from the stack, representing the score accumulated at the closing level.
   - We check for nested or matched same level closing bracket (popped value of 0).
   - If it's a nested closing bracket, we calculate the score for the previous nested levels (double the current level's score) and add it 
   to the score on the remaining level (previous level) in the stack. Otherwise, we add 1 to the new top of the stack.

"""
