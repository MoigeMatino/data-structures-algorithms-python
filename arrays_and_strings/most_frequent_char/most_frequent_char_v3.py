def most_frequent_char(s):
    """
    Finds the most frequent character in a string.

    Args:
        s (str): The input string.

    Returns:
        str: The most frequent character in the string, or None if there's a tie.
    """

    # Create a dictionary to track character frequencies
    tracker = {}
    for char in s:
        # Increment the count of the current character if it exists in the dictionary
        tracker[char] = tracker.get(char, 0) + 1

    # Find the key with the maximum value using max() and a custom key function
    most_frequent = max(tracker, key=tracker.get)

    return most_frequent

# Time Complexity: O(n)
# The code iterates through the string once to build the character frequency dictionary (O(n)).
# The `max` function with a custom key is also considered linear time (O(n)) in Python.

# Space Complexity: O(n)
# The `tracker` dictionary stores character frequencies, potentially holding all unique characters from the string.
# In the worst case, this leads to a space complexity of O(n).

# Reasoning and Approach:
# This code uses a dictionary and the `max` function with a custom key to efficiently find the most frequent character.
# 1. **Character Frequency Tracking:** It iterates through the string and builds a dictionary (`tracker`) where each key is a character and the value is its frequency (number of occurrences).
# 2. **Finding the Most Frequent Character (or First in Case of Tie):** It uses the `max` function to find the key (character) in the `tracker` dictionary with the maximum value (highest frequency).
#    The `key` argument in `max` specifies a custom function (`tracker.get`) that retrieves the corresponding value (frequency) for each key (character) during the comparison process.
# 3. **Tie Handling (Implicit):** Since the code doesn't explicitly check for ties, the first character encountered with the maximum frequency will be returned by `max`.
