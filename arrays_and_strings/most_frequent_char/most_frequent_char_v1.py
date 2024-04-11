def most_frequent_char(s):
    """
    Finds the most frequent character in a string.

    Args:
        s (str): The input string.

    Returns:
        str: The most frequent character in the string, or None if the string is empty.
    """

    # Create a dictionary to track character frequencies
    tracker = {}
    for char in s:
        # Increment the count of the current character if it exists in the dictionary
        tracker[char] = tracker.get(char, 0) + 1  # Use get() with default 0

    # Initialize a variable to track the most frequent character (and its count)
    proxy = None

    # Iterate through the string again to find the character with the highest count
    for char in s:
        # If there's no current leader (proxy) or the current character's count is higher:
        if not proxy or tracker[char] > tracker[proxy]:
            # Update the proxy with the current character
            proxy = char

    return proxy

# Example usage
print(most_frequent_char("aabbc"))  # Output: "b"

# Time Complexity: O(n)
# The code iterates through the string twice:
#   - Once to build the character frequency dictionary (O(n)).
#   - Once to find the most frequent character using the dictionary (O(n)).

# Space Complexity: O(n)
# The `tracker` dictionary stores character frequencies, potentially holding all unique characters from the string.
# In the worst case, this leads to a space complexity of O(n).

# Reasoning and Approach:
# This code uses a two-pass approach to find the most frequent character.
# 1. **Character Frequency Tracking:** It iterates through the string and builds a dictionary (`tracker`) where each key is a character and the value is its frequency (number of occurrences).
# 2. **Finding the Most Frequent Character:** It iterates through the string again. It keeps track of a potential leader (`proxy`) which is the most frequent character encountered so far. 
#    It compares the frequency of the current character with the `proxy`. If the current character's frequency is higher, it becomes the new `proxy`.
# This approach leverages a dictionary for efficient frequency tracking and avoids unnecessary computations, resulting in a time complexity of O(n).

# Why the Proxy?
# The `proxy` variable is used to efficiently track the current leading candidate for the most frequent character. 
# During the second iteration, as the code iterates through each character, it compares its frequency with the current `proxy`. 
# If the current character's frequency is higher, it updates the `proxy` with this new character. 
# By keeping track of this potential leader, the code avoids unnecessary comparisons and focuses only on characters that could potentially be more frequent than the current leader.
