def max_palin_subsequence(string):
    """
    This function finds the length of the longest palindromic subsequence in a given string.

    Args:
        string (str): The input string.

    Returns:
        int: The length of the longest palindromic subsequence.
    """
    # get the index of last element
    end = len(string) - 1

    # declare the dictionary
    memo = {}
    
    # Helper function to perform the actual palindromic subsequence calculation with memoization
    return _max_palin_subsequence(string, 0, end , memo)


def _max_palin_subsequence(string, start, end, memo):
    """
    This helper function recursively calculates the length of the longest palindromic subsequence
    in a substring of the given string using memoization to avoid redundant calculations.

    Args:
        string (str): The input string.
        start (int): The starting index of the substring.
        end (int): The ending index of the substring (inclusive).
        memo (dict): A dictionary to store previously calculated results for overlapping substrings.

    Returns:
        int: The length of the longest palindromic subsequence in the substring.
    """

    # Create a key to store the result for the current substring in the memoization dictionary
    key = (start, end)

    # Check if the result for the current substring has already been calculated and memoized
    if key in memo:
        return memo[key]

    # Base cases:
    # If the substring is of length 1, then the longest palindromic subsequence is the character itself (length 1)
    if start == end:
        return 1

    # If the starting index is greater than the ending index, there is no palindromic subsequence (length 0)
    if start > end:
        return 0

    # Check if the characters at the starting and ending indexes are the same
    if string[start] == string[end]:
        # If the characters are the same, the length of the longest palindromic subsequence is 2 (including the current characters)
        # plus the length of the longest palindromic subsequence in the remaining substring (excluding the current characters)
        memo[key] = 2 + _max_palin_subsequence(string, start + 1, end - 1, memo)
    else:
        # If the characters are different, we need to consider two options:
        # 1. Exclude the character at the starting index and find the longest palindromic subsequence in the remaining substring.
        # 2. Exclude the character at the ending index and find the longest palindromic subsequence in the remaining substring.
        # The length of the longest palindromic subsequence will be the maximum of these two options.
        memo[key] = max(
            _max_palin_subsequence(string, start + 1, end, memo),
            _max_palin_subsequence(string, start, end - 1, memo),
        )

    # Return the calculated length of the longest palindromic subsequence for the current substring
    return memo[key]

"""
Time Complexity:
The time complexity of this algorithm is O(n^2), where n is the length of the input string.
Each recursive call can lead to two further recursive calls, and we memoize the results to avoid redundant computations.

Space Complexity:
The space complexity is O(n^2) as well, due to the memoization dictionary. We store n^2 keys in the memo.

Notes:
This algorithm uses dynamic programming with memoization to efficiently find the length of the longest palindromic subsequence.
We start with two pointers, one at the beginning and the other at the end of the string, and move them inward, 
recursively checking if the characters at these positions are equal.
If they are equal, we increment the length of the palindromic subsequence by 2.
If not, we explore both possibilities by either moving the left pointer or the right pointer inward and choose the maximum of the two results.
"""
