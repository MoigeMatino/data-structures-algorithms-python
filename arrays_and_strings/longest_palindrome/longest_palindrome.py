from collections import defaultdict


def longest_palindrome(s: str) -> int:
  """
  Finds the length of the longest palindrome that can be formed from the given string.

  This function takes a string `s` as input and returns the length of the longest palindromic substring that
  can be formed by rearranging the characters in the string. A palindrome is a word or phrase that reads the
  same backward as forward (e.g., "racecar", "madam").

  Args:
      s (str): The input string.

  Returns:
      int: The length of the longest palindrome that can be formed from the string.
  """

  # Initialize a dictionary to store character counts (defaultdict provides a default value of 0)
  count_map = defaultdict(int)
  has_odd_count = False  # Flag to track if there's a character with odd frequency
  max_palindrome = 0  # Variable to store the maximum palindrome length

  # Count the frequency of each character in the string
  for char in s:
    count_map[char] += 1

  # Edge case: If the string has only one unique character, return its count (entire string is a palindrome)
  if len(count_map) == 1:
    for char in count_map:
      return count_map[char]

  # Iterate through the character counts
  for count in count_map.values():
    # If a character has odd frequency, set the flag and add even part of the count to max_palindrome
    if count % 2 == 1:
      has_odd_count = True
      max_palindrome += (count // 2) * 2
    # If a character has even frequency, add its entire count (both halves can be used)
    else:
      max_palindrome += count

  # If there's a character with odd frequency, add 1 to the max_palindrome (center of the palindrome)
  if has_odd_count:
    max_palindrome += 1

  return max_palindrome

# Time Complexity: O(n)
# The time complexity of this algorithm is O(n) where n is the length of the input string. This is because:
# * The loop iterating through the characters in the string runs n times.
# * The operations inside the loop (incrementing count and checking for odd/even frequency) are constant time.

# Space Complexity: O(n)
# The space complexity of this algorithm is O(n) due to the `count_map` dictionary that stores character counts.
# In the worst case, the dictionary can hold up to n unique characters from the string.

# Note:
# This algorithm utilizes a dictionary (`defaultdict`) to efficiently count character frequencies. It iterates
# through the string once and builds the frequency map. Then, it iterates through the character counts and
# calculates the maximum palindrome length based on even and odd frequencies. The key insight is that a
# palindrome can be formed using even occurrences of characters (both halves can be used) and at most one
# character with an odd occurrence (center of the palindrome).
