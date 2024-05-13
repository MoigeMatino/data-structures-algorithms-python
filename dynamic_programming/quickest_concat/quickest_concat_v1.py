from typing import Union

def quickest_concat(s: str) -> int:
    """
    Finds the minimum number of words required to concatenate the given string using words from a list.

    Args:
        s (str): The target string.

    Returns:
        int: The minimum number of words required to form the string, or -1 if it's not possible.

    This function implements a recursive approach to find the minimum number of words needed to
    concatenate the target string (`s`) using words from a provided list (`words`). The function utilizes
    a helper function (`_quickest_concat`) that performs the core logic.

    - If the target string is empty, no words are needed (return 0).
    - The function iterates through each word in the list.
    - If the target string starts with the current word:
        - Extract the remaining suffix of the target string after removing the matching word.
        - Recursively call `_quickest_concat` on the suffix and the word list to find the minimum
          number of words needed to form the remaining string.
        - Add 1 (for the current word) to the result from the recursive call.
        - Update `min_words` to store the minimum number of words found so far (including the current word).
    - If no word in the list matches the beginning of the target string, the function cannot
      form the string and returns positive infinity (indicating an error).
    - Finally, the `quickest_concat` function checks the returned value from the helper. If it's positive
      infinity, it means the string cannot be formed, so -1 is returned. Otherwise, the minimum number
      of words is returned.
    """

    result = _quickest_concat(s, words)
    if result == float('inf'):
        return -1
    return result


def _quickest_concat(s: str, words: list[str]) -> Union[float, int]:
    """
    Helper function for finding the minimum number of words to concatenate the string.

    Args:
        s (str): The target string.
        words (list[str]): The list of words to use for concatenation.

    Returns:
        Union[float, int]: The minimum number of words required (int), or positive infinity (float)
                           if the string cannot be formed.
    """

    if len(s) == 0:  # Base case: Empty string requires no words
        return 0

    min_words = float('inf')  # Initialize minimum words to positive infinity

    for word in words:
        if s.startswith(word):  # Check if the word is a prefix of the target string
            suffix = s[len(word):]  # Extract the remaining suffix after removing the matching word
            num_words = 1 + _quickest_concat(suffix, words)  # Recursive call with remaining string
            min_words = min(num_words, min_words)  # Update minimum if a better solution is found

    return min_words  # Return the minimum number of words found
# Time Complexity:

#     The time complexity of this algorithm is O(n * m), where n is the length of the target string and m is the number of words in the list.
#     In the worst case, the function needs to iterate through all words in the list for each substring of the target string, leading to this complexity.

# Space Complexity:

#     The space complexity of this algorithm is O(n) due to the recursive calls. The recursive stack can grow up to a depth equal to the length of the target string in the worst case.
