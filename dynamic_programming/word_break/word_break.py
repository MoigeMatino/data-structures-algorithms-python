def word_break(s: str, words: list[str]) -> list[str]:
    """
    This function finds all possible ways to segment a string into space-separated sequences of words
    from a given dictionary (words set).

    Args:
        s (str): The input string to be segmented.
        words (set[str]): The set of words allowed for segmentation.

    Returns:
        list[str]: A list containing all possible valid word segmentation combinations for the input string
                   (space-separated word sequences). If no segmentation is possible, an empty list is returned.
    """

    # Memoization dictionary to store previously computed results and avoid redundant calculations
    memo = {}

    # Call the helper function to perform word break recursion with memoization
    sentences = _word_break(s, words, memo)

    return sentences


def _word_break(s: str, words: list[str], memo: dict) -> list[str]:
    """
    This helper function recursively explores all possible word segmentations for a given string
    using memoization to store previously computed results.

    Args:
        s (str): The input string to be segmented.
        words (set[str]): The set of words allowed for segmentation.
        memo (dict): A dictionary to store previously computed results for specific substrings.

    Returns:
        list[str]: A list containing all possible valid word segmentation combinations for the input string
                   (space-separated word sequences). If no segmentation is possible, an empty list is returned.
    """

    # Check if the segmentation result for this string is already memoized
    if s in memo:
        return memo[s]

    # Base case: If the string is empty, it's a valid segmentation (empty sentence)
    if s == "":
        return [""]  # Return an empty string as one valid segmentation option

    sentences = []  # List to store all valid segmentations for the current string
    for word in words:
        # Check if the current word is a prefix of the string
        if s.startswith(word):
            suffix = s[len(word):]  # Extract the remaining string after the matching word
            suffix_sentences = _word_break(suffix, words, memo)  # Recursively explore segmentations for the suffix

            # Consider only non-empty suffix segmentations to avoid redundant single-word options 
            # (e.g., "catsanddog" should not have "cat" followed by an empty string)
            for sentence in suffix_sentences:
                if sentence:
                    # Combine the current word with a valid segmentation of the suffix
                    sentences.append(word + " " + sentence)
                else:
                    # If the suffix segmentation is empty, consider the current word itself as a valid segmentation
                    sentences.append(word)

    # Memoize the segmentation results for the current string before returning
    memo[s] = sentences
    return memo[s]
