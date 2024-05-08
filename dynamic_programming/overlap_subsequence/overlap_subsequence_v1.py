def overlap_subsequence(s1: str, s2: str) -> int:
    """
    This function finds the length of the longest common subsequence between two strings.

    Args:
        s1 (str): The first input string.
        s2 (str): The second input string.

    Returns:
        int: The length of the longest common subsequence between the two strings.
    """

    # Helper function to perform the actual overlap subsequence calculation
    return _overlap_subsequence(s1, s2, 0, 0)


def _overlap_subsequence(s1: str, s2: str, idx1: int, idx2: int) -> int:
    """
    This helper function recursively calculates the length of the longest common subsequence
    between two strings.

    Args:
        s1 (str): The first input string.
        s2 (str): The second input string.
        idx1 (int): The index of the current character in string_1.
        idx2 (int): The index of the current character in string_2.

    Returns:
        int: The length of the longest common subsequence between the two strings starting from the current indices.
    """

    # Base case: If we reach the end of either string, then the longest common subsequence length is 0
    if idx1 == len(s1) or idx2 == len(s2):
        return 0

    # Check if the characters at the current indices are the same
    if s1[idx1] == s2[idx2]:
        # If the characters are the same, the length of the longest common subsequence is 1 (including the current characters)
        # plus the length of the longest common subsequence in the remaining subsequences (excluding the current characters)
        return 1 + _overlap_subsequence(s1, s2, idx1 + 1, idx2 + 1)
    else:
        # If the characters are different, consider two options:
        #   - Exclude the character at the current index in s1 and find the longest common subsequence in the remaining subsequences.
        #   - Exclude the character at the current index in s2 and find the longest common subsequence in the remaining subsequences.
        # The length of the longest common subsequence will be the maximum of these two options.
        without_s1_prefix = _overlap_subsequence(s1, s2, idx1 + 1, idx2)  # Exclude s1[idx1]
        without_s2_prefix = _overlap_subsequence(s1, s2, idx1, idx2 + 1)  # Exclude s2[idx2]
        return max(without_s1_prefix, without_s2_prefix)

# Time Complexity: O(m * n)
# The time complexity of this algorithm is O(m * n), where m and n are the lengths of the two input strings. This is because the 
# _overlap_subsequence function makes recursive calls for all possible combinations of indices in the two strings. In the worst case, 
# each subproblem is solved once, resulting in m * n time complexity.

# Space Complexity: O(m * n)
# The space complexity of this algorithm is O(m * n) due to the recursion call stack. In the worst case, the recursion can go up to a 
# depth of m (for string 1) and n (for string 2) levels, leading to O(m * n) space complexity.

# Approach and Reasoning:
# This algorithm uses a recursive approach with the concept of dynamic programming to solve the longest common subsequence problem. 
# It breaks down the problem into smaller subproblems of finding the longest common subsequence between suffixes of the two strings starting 
# from specific indices. The core logic relies on the observation that if the characters at the current indices of the two strings are the same, 
# then the longest common subsequence can be formed by including those characters and finding the longest common subsequence in the remaining 
# suffixes (excluding those characters). Otherwise, the longest common subsequence is the maximum of the longest common subsequences obtained by 
# excluding the character at the current index in either string.
