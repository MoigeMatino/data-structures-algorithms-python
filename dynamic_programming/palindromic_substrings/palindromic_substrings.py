from typing import Dict, Tuple


def count_palindromic_substrings(s: str) -> int:
  """
  Counts the total number of palindromic substrings in a given string.

  This function takes a string `s` as input and iterates through all possible substrings.
  For each substring (defined by start and end indices), it checks if it's a palindrome
  using a helper function `is_palindrome`. The total count of palindromic substrings is returned.

  Args:
      s: The input string.

  Returns:
      The total number of palindromic substrings in the input string.
  """

  total_palindromes = 0  # Initialize a variable to count palindromes
  memo = {}  # Create a dictionary to store palindrome check results (memoization)

  # Iterate through all possible substrings starting from each character in the string
  for start in range(len(s)):
    for end in range(start, len(s)):
      if is_palindrome(s, start, end, memo):  # Check if current substring is a palindrome
        total_palindromes += 1

  return total_palindromes


def is_palindrome(s: str, start: int, end: int, memo: Dict[Tuple[int, int], bool]) -> bool:
  """
  Checks if a given substring is a palindrome using memoization.

  This function takes a string `s`, starting index `start`, ending index `end`, and a memoization
  dictionary as input. It checks if the palindrome status for this substring is already stored
  in the memo. If not, it performs the following checks:
  - Base cases: If start and end are the same (single character) or if start is greater than
    end (empty substring), it's considered a palindrome.
  - If the first and last characters are the same, it recursively checks if the remaining substring
    (excluding the first and last characters) is a palindrome using memoization.
  - The result is stored in the memo dictionary for future reference and returned.

  Args:
      s: The input string.
      start: The starting index of the substring.
      end: The ending index of the substring.
      memo: A dictionary to store palindrome check results for substrings (memoization).

  Returns:
      True if the given substring is a palindrome, False otherwise.
  """

  key = start, end  # Create a unique key for the substring (start, end)

  if key in memo:
    return memo[key]  # Return cached result if available

  # Base cases: single character or empty substring
  if start == end:
    return True
  if start > end:
    return False

  # Check if first and last characters match, then check remaining substring
  if s[start] == s[end]:
    if end - start == 1 or is_palindrome(s, start + 1, end - 1, memo):
      memo[key] = True
      return True

  memo[key] = False  # Store 'False' if not a palindrome for future reference
  return False


# Time Complexity: O(n^3) in the worst case.
# The outer loop iterates through all possible substrings (n choices for start and n choices for end
# for each start), leading to n^2 iterations. The inner loop (is_palindrome) can potentially call itself
# for each substring, resulting in O(n) additional time in the worst case. In total, the time complexity
# becomes O(n^2 * n) = O(n^3).

# Space Complexity: O(n^2) in the worst case.
# The memo dictionary stores the palindrome check results for all possible substrings. In the worst case,
# all substrings might be unique, leading to a space complexity of O(n^2).

# Note:
# This approach utilizes memoization to avoid redundant palindrome checks for overlapping substrings.
# By storing the results in a dictionary, the function can efficiently determine if a substring is a
# palindrome by checking the memo before performing the recursive check again. This significantly improves
# performance compared to a naive approach that checks every substring independently. 
