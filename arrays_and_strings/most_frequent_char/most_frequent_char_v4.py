from collections import Counter

def most_frequent_char(s):
    """
    Finds the most frequent character in a string.

    Args:
        s (str): The input string.

    Returns:
        str: The most frequent character in the string, or None if the string is empty.
    """

    # Create a Counter object to efficiently track character frequencies
    tracker = Counter(s)

    # Initialize a variable to track the most frequent character (and its count)
    most_frequent_char = None

    # Iterate through the string to find the character with the highest count
    for char in s:
        # If there's no current leader (most_frequent_char) or the current character's count is higher:
        if most_frequent_char is None or tracker[char] > tracker[most_frequent_char]:
            # Update the most_frequent_char with the current character
            most_frequent_char = char

    return most_frequent_char

# Time Complexity: O(n)
# The code iterates through the string once (O(n)) to create the Counter object 
# (which efficiently counts character frequencies) and then iterates through it again (O(n)) 
# to find the most frequent character.

# Space Complexity: O(n)
# The `tracker` Counter object stores character frequencies, potentially holding all unique characters from the string.
# In the worst case, this leads to a space complexity of O(n).

# Reasoning and Approach:
# This code leverages the `Counter` class from the `collections` module for efficient character frequency counting and finding the most frequent one.
# 1. **Character Frequency Tracking:** It creates a `Counter` object (`tracker`) from the input string. 
#    The `Counter` constructor automatically counts the occurrences of each character in the string, 
#    providing efficient access to character frequencies.
# 2. **Finding the Most Frequent Character:** It iterates through the string again. 
#    It keeps track of a potential leader (`most_frequent_char`) which is the most frequent character encountered so far. 
#    During each iteration, it compares the current character's frequency (using `tracker[char]`) with the `most_frequent_char`. 
#    If the current character's frequency is higher, it becomes the new `most_frequent_char`.
# This approach utilizes the built-in functionality of `Counter` to streamline character counting and comparison, resulting in a time complexity of O(n).
