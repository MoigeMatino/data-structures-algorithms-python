from collections import Counter

def anagrams(s1, s2):
    """
    Checks if two strings are anagrams (have the same characters with the same frequency).

    Args:
        s1 (str): The first string.
        s2 (str): The second string.

    Returns:
        bool: True if the strings are anagrams, False otherwise.
    """

    # Create frequency counters for both strings using the Counter class
    s1_dict = Counter(s1)  # Count character occurrences in s1
    s2_dict = Counter(s2)  # Count character occurrences in s2

    # Check if the character counts are equal (same characters with same frequencies)
    return s1_dict == s2_dict

# Time Complexity: O(n + m)
# The `Counter` constructor iterates through each character in the input string (n or m characters).
# In the worst case, it needs to iterate through all characters. This results in a linear time complexity of O(n) for each string.
# The `anagrams` function calls `Counter` twice, leading to a combined time complexity of O(n + m).

# Space Complexity: O(n + m)
# Both `anagrams` creates Counter objects (dictionaries) to store character frequencies.
# In the worst case, each Counter object can hold all unique characters from the respective strings.
# This leads to a space complexity of O(n) for each string and O(n + m) overall.

# Reasoning and Approach:
# This code utilizes the `Counter` class from the `collections` module for efficient anagram checking.
# `Counter` provides a dictionary-like object that automatically counts the occurrences of elements in an iterable (like a string).
# The code creates Counter objects for both strings (`s1_dict` and `s2_dict`). These objects efficiently store the frequency of each character.
# Finally, it compares these counters using the `==` operator, which checks if they have the same keys (characters) with the same values (frequencies).
# This approach leverages the built-in functionality of `Counter` for efficient character counting and comparison, resulting in a time complexity of O(n + m).
