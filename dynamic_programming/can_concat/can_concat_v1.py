def can_concatenate(s: str, words: list[str]) -> bool:
    """
    This function checks whether a target string can be formed by concatenating words from a given word list (without reusing words).

    Args:
        s (str): The target string.
        words (list[str]): The list of words to be used for concatenation.

    Returns:
        bool: True if the target string can be formed by concatenating words from the word list, False otherwise.
    """

    # Base case: If the target string is empty, it can be formed by concatenating no words (empty string)
    if len(s) == 0:
        return True

    # Iterate through each word in the word list
    for word in words:
        # Check if the target string starts with the current word
        if s.startswith(word):
            # Get the remaining suffix of the target string after removing the current word
            suffix = s[len(word):]
            # Recursively check if the remaining suffix can be formed by concatenating words from the list
            if can_concatenate(suffix, words) == True:
                # If the suffix can be formed, return True
                return True

    # If no word in the list is a prefix of the target string or the remaining suffix cannot be formed, return False
    return False

# Time Complexity: O(s ^ w) in the worst case
# The time complexity of this algorithm can be O(s * w) in the worst case, where s is the length of the target string and w is the number of words in the list. 
# In the worst case, the function will have to explore all possible concatenations, leading to exponential time complexity.

# Space Complexity: O(s)
# The space complexity of this algorithm is O(s) due to the recursion call stack. In the worst case, the recursion can go up to a depth of s (for a string of length s), 
# leading to O(s) space complexity.

# Approach and Reasoning:
# This algorithm uses a recursive approach to solve the can_concatenate problem. It breaks down the problem into smaller subproblems of checking if a suffix of the 
# target string can be formed by concatenating words from the list. The core logic relies on the observation that if a target string starts with a word in the list, 
# then the target string can be formed by concatenating that word and checking if the remaining suffix can be formed by concatenating words from the list. 
