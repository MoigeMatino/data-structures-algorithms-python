def paired_parentheses(string):
  """
  Checks if a string contains well-formed and matching parentheses '()'.

  Args:
      string: The string to be checked for balanced parentheses. The string can
              only contain opening and closing parentheses '()'.

  Returns:
      True if the string contains well-formed and matching parentheses, False otherwise.
  """

  opening = '('  # Constant representing the opening parenthesis
  closing = ')'  # Constant representing the closing parenthesis
  stack = []  # Stack to keep track of encountered opening parentheses

  for char in string:
    if char == opening:  # Check if character is an opening parenthesis
      """
      # Push opening parenthesis onto stack
      If the character is an opening parenthesis, push it onto the stack. This indicates
      that we need to find its corresponding closing parenthesis later.
      """
      stack.append(char)
    elif char == closing:  # Check if character is a closing parenthesis
      """
      # Handle closing parenthesis
      If the character is a closing parenthesis:
        - Check if the stack is empty (unmatched closing parenthesis at the beginning).
        - If the stack is not empty, pop the most recent opening parenthesis from the stack.
      """
      if stack:
        stack.pop()
      else:
        return False  # Unmatched closing parenthesis (extra closing bracket)

  # After iterating through the string
  if stack:  # Check if all parentheses are matched (empty stack)
    """
    # Check for unmatched opening parentheses
    If the stack is not empty after iterating through the string, it signifies unmatched
    opening parentheses at the end.
    """
    return False
  else:
    return True

"""
Complexity Analysis

n is the length of the input string

Time Complexity: O(n)
The algorithm iterates through the string once (O(n)) and performs constant time operations (O(1)) like stack push/pop 
and comparisons. In the average case, the number of stack operations is proportional to the number of opening parentheses, 
which is typically less than or equal to the string length.

Space Complexity: O(n)
The stack can grow up to a depth equal to the number of opening parentheses in the string. In the worst case, all brackets 
might be opening parentheses, leading to a stack size of n. However, for well-formed strings with matching parentheses, the 
stack size will be balanced and typically much smaller than n.

Further Notes:

* The algorithm efficiently checks for balanced parentheses using a stack data structure.
* It returns False for unmatched closing parentheses or strings with extra closing parentheses.
* It also returns False for strings with unmatched opening parentheses at the end.

Approach Reasoning:

This algorithm utilizes a stack to keep track of encountered opening parentheses. As we iterate through the string:

1. If a character is an opening parenthesis, it's pushed onto the stack.
2. If a character is a closing parenthesis:
   * We check if the stack is empty (indicating an unmatched closing bracket at the beginning).
   * If the stack is not empty, we pop the most recent opening parenthesis from the stack. This ensures that the closing parenthesis 
   matches the most recent opening parenthesis encountered.
"""
