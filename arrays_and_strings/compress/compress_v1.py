def compress(s):
    """
    Compresses a string by replacing repeated characters with a count followed by the character.

    Args:
        s (str): The string to be compressed.

    Returns:
        str: The compressed string.
    """

    # Add a special character to signal the end of the string during processing
    s += '@'
    result = ''
    i = 0  # Starting index of the current character sequence
    j = 0  # Index iterating through the string

    while j < len(s):
        if s[i] == s[j]:
            # Characters are the same, increment the ending index
            j += 1
        else:
            # Encountered a different character, process the previous sequence
            count = j - i  # Calculate the number of repeated characters
            if count == 1:
                # If only one character, append it directly
                result += s[i]
            else:
                # Otherwise, append the count and the character
                result += str(count) + s[i]
            # Move the starting index to the current character
            i = j
            j += 1

    return result

# Time Complexity: O(n^2) in the worst case
# String concatenation in Python creates a new string, potentially leading to n iterations
# with linear time complexity (O(n)) for copying the existing string content.
# This concatenation nested within the loop structure can result in overall time complexity of O(n^2).

# Space Complexity: O(n)
# The `result` string grows as characters are appended during compression,
# potentially reaching a size of n (where n is the length of the input string).
# There's also additional space usage for temporary variables like `i` and `j`.
# However, these temporary variables have a constant space complexity and don't
# significantly affect the overall space complexity dominated by the `result` string.

# Reasoning and Approach:
# This code implements a simple compression algorithm using two pointers (`i` and `j`).
# It iterates through the string and identifies sequences of repeated characters.
# The code counts the number of repetitions and appends either the single character
# (if repeated once) or the count followed by the character to a new string (`result`).
# While this approach is easy to understand, it's important to note the potential
# time complexity drawback due to string concatenation in the worst case.
