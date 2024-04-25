def overlap_subsequence(string_1, string_2):
    """
    This function finds the length of the longest common subsequence between two strings.

    Args:
        string_1 (str): The first input string.
        string_2 (str): The second input string.

    Returns:
        int: The length of the longest common subsequence between the two strings.
    """

    # Helper function to perform the actual overlap subsequence calculation with memoization
    return _overlap_subsequence(string_1, string_2, 0, 0, {})


def _overlap_subsequence(string_1, string_2, i, j, memo):
    """
    This helper function recursively calculates the length of the longest common subsequence
    between two strings using memoization to avoid redundant calculations.

    Args:
        string_1 (str): The first input string.
        string_2 (str): The second input string.
        i (int): The index of the current character in string_1.
        j (int): The index of the current character in string_2.
        memo (dict): A dictionary to store previously calculated results for overlapping subsequences.

    Returns:
        int: The length of the longest common subsequence between the two strings starting from the current indices.
    """

    # Create a key to store the result for the current substring in the memoization dictionary
    key = (i, j)

    # Check if the result for the current substring has already been calculated and memoized
    if key in memo:
        return memo[key]

    # Base cases:
    # If we reach the end of either string, then the longest common subsequence length is 0
    if i == len(string_1) or j == len(string_2):
        return 0

    # Check if the characters at the current indices are the same
    if string_1[i] == string_2[j]:
        # If the characters are the same, the length of the longest common subsequence is 1 (including the current characters)
        # plus the length of the longest common subsequence in the remaining subsequences (excluding the current characters)
        memo[key] = 1 + _overlap_subsequence(string_1, string_2, i + 1, j + 1, memo)
    else:
        # If the characters are different, we need to consider two options:
        # 1. Exclude the character at the current index in string_1 and find the longest common subsequence in the remaining subsequences.
        # 2. Exclude the character at the current index in string_2 and find the longest common subsequence in the remaining subsequences.
        # The length of the longest common subsequence will be the maximum of these two options.
        memo[key] = max(
            _overlap_subsequence(string_1, string_2, i + 1, j, memo),
            _overlap_subsequence(string_1, string_2, i, j + 1, memo),
        )

    # Return the calculated length of the longest common subsequence for the current substring
    return memo[key]


# Time Complexity:
# The time complexity of this algorithm is O(n * m), where n and m are the lengths of string_1 and string_2 respectively.
# The algorithm explores all possible subsequences by either moving to the next character in string_1 or string_2.

# Space Complexity:
# The space complexity is O(n * m) due to the memoization dictionary.
# Each unique pair of indices (i, j) is stored in the memoization dictionary.

# Notes:
# This algorithm uses dynamic programming with memoization to efficiently find the length of the longest common overlap subsequence.
# We start with two pointers, one for each string, and recursively check if the characters at these positions are equal.
# If they are equal, we increment the length of the overlap subsequence by 1 and move both pointers forward.
# If not, we explore both possibilities by either moving the pointer for string_1 or string_2 forward and choose the maximum of the two results.
