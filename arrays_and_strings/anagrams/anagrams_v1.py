def count_map(s):
    """
    Creates a dictionary to map characters in a string to their frequencies.

    Args:
        s (str): The input string.

    Returns:
        dict: A dictionary where keys are characters and values are their frequencies.
    """

    # Initialize an empty dictionary to store character counts
    count_dict = {}
    for char in s:
        # Iterate through each character in the string
        if char in count_dict:
            # If the character already exists in the dictionary, increment its count
            count_dict[char] += 1
        else:
            # If the character is new, add it to the dictionary with a count of 1
            count_dict[char] = 1

    return count_dict

def anagrams(s1, s2):
    """
    Checks if two strings are anagrams (have the same characters with the same frequency).

    Args:
        s1 (str): The first string.
        s2 (str): The second string.

    Returns:
        bool: True if the strings are anagrams, False otherwise.
    """

    # Create frequency maps for both strings using the count_map function
    char_map_1 = count_map(s1)
    char_map_2 = count_map(s2)

    # Check if the frequency maps are equal (same characters with same counts)
    return char_map_1 == char_map_2

# Time Complexity: O(n + m)
# The `count_map` function iterates through each character in the input string (n or m characters).
# In the worst case, it needs to iterate through all characters. This results in a linear time complexity of O(n) for each string.
# The `anagrams` function calls `count_map` twice, leading to a combined time complexity of O(n + m).

# Space Complexity: O(n + m)
# Both `count_map` and `anagrams` create dictionaries to store character frequencies.
# In the worst case, each dictionary can hold all unique characters from the respective strings.
# This leads to a space complexity of O(n) for each string and O(n + m) overall.

# Reasoning and Approach:
# This code utilizes a two-step approach to check for anagrams.
# 1. **Character Frequency Mapping:** The `count_map` function creates a dictionary for each string.
#    It iterates through the string and keeps track of the frequency of each character.
# 2. **Comparison of Frequency Maps:** The `anagrams` function compares the dictionaries created by `count_map` for both strings.
#    If the dictionaries are equal (meaning both strings have the same characters with the same frequencies), the strings are anagrams.
# This approach leverages dictionaries to efficiently store and compare character frequencies, resulting in a time complexity of O(n + m).
