def paired_parentheses(string):
  """
  Checks if a string contains well-formed and matching parentheses '()'.

  Args:
      string: The string to be checked for balanced parentheses. The string can
              only contain opening and closing parentheses '()'.

  Returns:
      True if the string contains well-formed and matching parentheses, False otherwise.
  """

  count_of_open_parentheses = 0  # Counter to track the number of opening parentheses

  for char in string:
    if char == '(':  # Check if character is an opening parenthesis
      """
      # Increment counter for opening parenthesis
      If the character is an opening parenthesis, increment the counter to keep track
      of how many opening parentheses have been encountered so far.
      """
      count_of_open_parentheses += 1
    elif char == ')':  # Check if character is a closing parenthesis
      """
      # Handle closing parenthesis
      If the character is a closing parenthesis:
        - Check for unmatched closing parenthesis:
          If the counter of opening parentheses is already 0, it signifies an unmatched
          closing parenthesis at the beginning or extra closing brackets at the end.
          Return False in that case.
        - Decrement counter for closing parenthesis:
          If there are opening parentheses encountered previously (counter > 0),
          decrement the counter to represent that a closing parenthesis matches an opening one.
      """
      if count_of_open_parentheses == 0:
        return False
      count_of_open_parentheses -= 1

  # After iterating through the string
  return count_of_open_parentheses == 0  # Check if all parentheses are matched (counter is 0)

"""
Complexity Analysis
n is the length of the input string

Time Complexity: O(n)
The algorithm iterates through the string once (O(n)) and performs constant time operations (O(1)) like comparisons, 
counter increments/decrements. In the average case, the number of operations is proportional to the number of parentheses, 
which is typically less than or equal to the string length.

Space Complexity: O(1)
This approach uses a single integer variable to track the counter. It doesn't require any additional data structures like stacks, 
leading to constant space complexity.

Notes:

* This approach is simpler and more efficient for basic balanced parenthesis checks.
* It might not be suitable for more complex scenarios involving nested parentheses or other bracket types.

Approach Reasoning:

This algorithm leverages a counter to keep track of the number of encountered opening parentheses. As we iterate through the string:

1. For an opening parenthesis '(':
   - We increment the counter to record that an opening parenthesis has been seen.
2. For a closing parenthesis ')':
   - We check if the counter is already 0 (unmatched closing parenthesis at the beginning).
   - If the counter is positive (opening parentheses encountered previously), we decrement it to signify that a closing parenthesis matches an opening one.
"""
