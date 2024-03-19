def befitting_brackets(string):
  """
  Checks if a string contains well-formed and matching brackets.

  Args:
      string: The string to be checked for balanced brackets. The string can
              contain various types of brackets: '(', ')', '{', '}', '[', ']'.

  Returns:
      True if the string contains well-formed and matching brackets, False otherwise.

  """

  braces_mapping = {  # Dictionary to map opening brackets to their closing counterparts
      '(': ')',
      '{': '}',
      '[': ']'
  }
  stack = []  # Stack to keep track of encountered opening brackets

  for char in string:
    if char in braces_mapping:  # Check if character is an opening bracket
      """
      # Push opening bracket onto stack
      If the character is an opening bracket, push it onto the stack. This indicates
      that we need to find its corresponding closing bracket later.
      """
      stack.append(char)
    else:
      if not stack:  # Check if stack is empty (unmatched closing bracket)
        """
        # Handle unmatched closing bracket
        If the character is a closing bracket and the stack is empty, it signifies an
        unmatched closing bracket at the beginning of the string or extra closing brackets
        at the end. Return a False in this case.
        """
        return False

      opening_brace = stack.pop()  # Pop the most recent opening bracket
      """
      # Check matching closing bracket
      If the character is a closing bracket, pop the most recent opening bracket
      from the stack. Compare the popped opening bracket with the current closing bracket
      using the braces_mapping dictionary. If they don't match, it indicates a mismatch.
      """
      if braces_mapping[opening_brace] != char:
        return False

  # After iterating through the string
  return len(stack) == 0  # Check if all brackets are matched (empty stack)

"""
Complexity Analysis
    n - length of the input string

Time Complexity: O(n) 
The algorithm iterates through the string once (O(n)) and performs constant time operations (O(1)) like dictionary 
lookups, stack push/pop, and comparisons. In the average case, the number of stack operations is proportional to the 
number of opening brackets, which is typically less than or equal to the string length.

Space Complexity: O(n)
The stack can grow up to a depth equal to the number of opening brackets in the string. In the worst case, all brackets 
might be opening brackets, leading to a stack size of n. However, for well-formed strings with matching brackets, the 
stack size will be balanced and typically much smaller than n.

Notes:

* The algorithm efficiently checks for balanced brackets using a stack data structure.
* It retruns a False for umatched closing or opening brackets.

Approach Reasoning:

This algorithm utilizes a stack to keep track of encountered opening brackets. As we iterate through the string:

1. If a character is an opening bracket, it's pushed onto the stack.
2. If a character is a closing bracket:
   * We check if the stack is empty (indicating an unmatched closing bracket at the beginning).
   * If the stack is not empty, we pop the most recent opening bracket from the stack.
   * We compare the popped opening bracket with the current closing bracket using a dictionary to ensure they are a matching pair.

"""
