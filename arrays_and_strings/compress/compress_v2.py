def compress(s):
    """
    Compresses a string by replacing repeated characters with a count followed by the character.

    Args:
        s (str): The string to be compressed.

    Returns:
        str: The compressed string.
    """

    # Add a special character to signal the end of the string during processing
    s += '!'
    result = []  # Use a list for efficient character appends
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
                result.append(s[i])  # Append character to result list
            else:
                # Otherwise, append the count and the character
                result.append(str(count))  # Append count as string
                result.append(s[i])  # Append character to result list
            # Move the starting index to the current character
            i = j
            j += 1

    # Convert the list of characters to a string for return
    return ''.join(result)

# Time Complexity: O(n)
# The code iterates through the string a maximum of n times (n being the string length).
# Appending elements to a list in Python is a constant time operation (O(1)).
# Therefore, the overall time complexity is linear (O(n)).

# Space Complexity: O(n)
# The `result` list grows as characters are appended during compression,
# potentially reaching a size of n (where n is the length of the input string).
# There's also additional space usage for temporary variables like `i`, `j`, and the special character.
# However, these temporary variables have a constant space complexity and don't
# significantly affect the overall space complexity dominated by the `result` list.

# Reasoning and Approach:
# This code utilizes a similar two-pointer approach as the previous version.
# It iterates through the string and identifies sequences of repeated characters.
# However, instead of creating a new string with each concatenation, it uses a list (`result`)
# to efficiently store the compressed characters. Appending to a list is a constant time operation,
# leading to an overall linear time complexity.
# The special character ('!') ensures proper handling of the last character sequence.
